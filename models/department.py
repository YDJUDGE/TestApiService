from . import Base

from sqlalchemy import (
    Column,
    String,
    ForeignKey
)

from . import TimestampMixin

class Deparment(Base):
    name_dep: str = Column(String(255), nullable=False)
    adress_dep = Column(String(200), nullable=False)

class Employee(TimestampMixin, Base):
    name: str = Column(String(255), nullable=False)

