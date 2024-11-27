# Создаём здесь сессию

from sqlalchemy.orm import (
    sessionmaker,
    Session as SessionType
)

from .base import engine

Session = sessionmaker(bind=engine, expire_on_commit=False)

def get_session() -> SessionType:
    with Session() as session:
        yield session
