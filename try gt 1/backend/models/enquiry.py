from datetime import datetime, timezone
import uuid

from pydantic import BaseModel, Field


class EnquiryCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    company: str = Field(min_length=2, max_length=160)
    email: str = Field(min_length=5, max_length=160)
    phone: str = Field(min_length=5, max_length=40)
    service_required: str = Field(min_length=2, max_length=120)
    message: str = Field(min_length=10, max_length=2000)


class Enquiry(EnquiryCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    reference_number: str = Field(
        default_factory=lambda: f"ZZZOR-{uuid.uuid4().hex[:4].upper()}"
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))