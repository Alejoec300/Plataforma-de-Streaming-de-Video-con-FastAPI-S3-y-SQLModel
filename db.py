from contextlib import asynccontextmanager

from sqlmodel import SQLModel, Session, create_engine

sqlite_url = "sqlite:///db.sqlite3"

engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
)


@asynccontextmanager
async def create_all_tables(app):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session