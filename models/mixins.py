from sqlalchemy import (
    Column,
    DateTime,
    func
)

from datetime import datetime

class TimestampMixin:
    created_at = Column(
        DateTime,
        default=datetime.utcnow(),
        server_default=func.now(),
        nullable=False
    )

