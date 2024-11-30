from . import Base

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer
)

from . import TimestampMixin

from sqlalchemy.orm import relationship

class Employee(TimestampMixin, Base):
    __tablename__ = "blog_employee"
    name: str = Column(String(255), nullable=False)
    dep_id: int = Column(Integer, ForeignKey("blog_departments.id"), nullable=False, unique=False)

    department = relationship("Deparment", back_populates="employee", uselist=False)

