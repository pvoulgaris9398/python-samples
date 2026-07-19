using System.Diagnostics;
using System.Text.Json;
using Microsoft.EntityFrameworkCore;
//using Microsoft.Extensions; // Standard namespaces
using Microsoft.Extensions.Caching.Distributed;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

var builder = WebApplication.CreateBuilder(args);

// ----------------------------------------------------
// 1. Storage & Caching Configurations
// ----------------------------------------------------
var postgresConn = "Host=localhost;Port=5432;Database=ecom_db;Username=dev_user;Password=dev_password";
var redisConn = "localhost:6379";

builder.Services.AddDbContext<AppDbContext>(options => options.UseNpgsql(postgresConn));
builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = redisConn;
    options.InstanceName = "Catalog_";
});

// Configures the typed gRPC client to point to the Python backend port
builder.Services.AddGrpcClient<DotnetApiGateway.Protos.InventoryService.InventoryServiceClient>(o =>
{
    o.Address = new Uri("http://localhost:50051");
});


// ----------------------------------------------------
// 2. OpenTelemetry & Distributed Tracing Setup
// ----------------------------------------------------
// Define a custom activity source for application-level trace spans
var appSource = new ActivitySource("DotnetApiGateway.Core");

builder.Services.AddOpenTelemetry()
    .WithTracing(tracing => tracing
        .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("DotnetApiGateway"))
        .AddSource("DotnetApiGateway.Core")
        .AddAspNetCoreInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddRedisInstrumentation() // Captures raw Redis commands automatically
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("http://localhost:4317"); // Targets your OTel Collector
        }));

var app = builder.Build();

// Auto-apply database schema migrations on startup
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    db.Database.EnsureCreated();
}

// ----------------------------------------------------
// 3. API Endpoints (Cache-Aside Pattern)
// ----------------------------------------------------
app.MapGet("/products/{id:int}", async (
    int id, 
    IDistributedCache cache, 
    AppDbContext db, 
    DotnetApiGateway.Protos.InventoryService.InventoryServiceClient inventoryClient) =>
{
    using var activity = appSource.StartActivity("GetProductDetail");
    activity?.SetTag("product.id", id);

    string cacheKey = $"product:{id}";
    string? cachedJson = await cache.GetStringAsync(cacheKey);
    Product? product;

    if (!string.IsNullOrEmpty(cachedJson))
    {
        activity?.SetTag("cache.hit", true);
        product = JsonSerializer.Deserialize<Product>(cachedJson);
    }
    else
    {
        activity?.SetTag("cache.hit", false);
        product = await db.Products.FindAsync(id);
        if (product is not null)
        {
            await cache.SetStringAsync(cacheKey, JsonSerializer.Serialize(product), 
                new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) });
        }
    }

    if (product is null) return Results.NotFound();

    // Chaining the request: Call Python FastAPI via gRPC
    // Tracing context is automatically injected into the request metadata headers here
    var stockResponse = await inventoryClient.CheckStockAsync(new DotnetApiGateway.Protos.StockRequest { ProductId = id });

    return Results.Ok(new {
        DataSource = !string.IsNullOrEmpty(cachedJson) ? "Redis Cache" : "PostgreSQL Database",
        Data = product,
        StockInfo = new {
            Available = stockResponse.AvailableStock,
            InStock = stockResponse.IsInStock
        }
    });
});


// Helper endpoint to populate seed data directly into PostgreSQL
app.MapPost("/products/seed", async (AppDbContext db) =>
{
    if (!await db.Products.AnyAsync())
    {
        db.Products.AddRange(
            new Product { Name = "Gaming Laptop", Price = 1299.99m },
            new Product { Name = "Wireless Mouse", Price = 49.99m },
            new Product { Name = "Mechanical Keyboard", Price = 89.99m }
        );
        await db.SaveChangesAsync();
        return Results.Ok("Database seeded successfully.");
    }
    return Results.Ok("Database already contains data.");
});

app.Run();

// ----------------------------------------------------
// 4. Data Models & Database Context
// ----------------------------------------------------
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public decimal Price { get; set; }
}

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
    public DbSet<Product> Products => Set<Product>();
}
