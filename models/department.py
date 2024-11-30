from . import Base

from sqlalchemy import (
    Column,
    String
)

from sqlalchemy.orm import relationship

class Deparment(Base):
    __tablename__ = "blog_departments"
    name_dep: str = Column(String(255), nullable=False)
    adress_dep: str = Column(String(200), nullable=False)


    employee = relationship("Employee", back_populates="department", uselist=True)
