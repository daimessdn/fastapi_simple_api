from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from config import Config

async_engine = AsyncEngine(create_engine(
    Config.DB_URL,
    echo=True
))


async def init_db():
    async with async_engine.begin() as conn:
        # create all tables - importing all models
        from v1.products.models import Product

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
