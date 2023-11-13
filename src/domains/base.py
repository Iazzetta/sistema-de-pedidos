from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from datetime import datetime


class DomainBase(BaseModel):
    id: UUID = Field(default=uuid4())
    created_at: datetime = Field(default_factory=datetime.now)
