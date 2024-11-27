from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship

from . import Base
from .mixins import TimestampMixin

class Order(TimestampMixin, Base):
    adress = Column(String, nullable=False)
    description = Column(String(100), default="", nullable=True)

    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=False
    )

    user = relationship("User", back_populates="orders")

