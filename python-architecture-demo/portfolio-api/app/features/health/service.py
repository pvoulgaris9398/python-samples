from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def get_database_health(db: AsyncSession) -> bool:
    result = await db.execute(text("select 1"))
    return bool(result.scalar_one())
