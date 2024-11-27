from uuid import uuid4

from . import Base


from sqlalchemy import (
    Column,
    String,
    Boolean
)

from sqlalchemy.orm import relationship

def generate_token():
    return str(uuid4())

class User(Base):
    username = Column(String(20), nullable=False, unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    email = Column(String(100), default="", nullable=True)

    token = Column(String, default=lambda: generate_token(), nullable=False, unique=True)

    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}",
            f"{self.id}",
            f"{self.username}",
            f"{self.is_staff}",
            f"{self.email}"

        )
