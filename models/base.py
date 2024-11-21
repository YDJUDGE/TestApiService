# Настройка базовой программы

from sqlalchemy import (
    create_engine,
    Column,
    Integer
)

from sqlalchemy.orm import (
    declarative_base,
    declared_attr
)

import config

class Base:

    @declared_attr
    def __tablename__(cls):
        """

        :return:
        """

    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    def __repr__(self):
        return str(self)

engine = create_engine(config.DB_URL, echo=config.DB_ECHO)
Base = declarative_base(cls=Base)
