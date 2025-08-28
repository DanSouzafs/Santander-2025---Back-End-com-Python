from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = Mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
