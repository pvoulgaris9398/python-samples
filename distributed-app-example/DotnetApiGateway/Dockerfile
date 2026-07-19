FROM ://microsoft.com AS build
WORKDIR /src
COPY ["DotnetApiGateway.csproj", "./"]
RUN dotnet restore "DotnetApiGateway.csproj"
COPY . .
RUN dotnet publish "DotnetApiGateway.csproj" -c Release -o /app/publish

FROM ://microsoft.com AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "DotnetApiGateway.dll"]
