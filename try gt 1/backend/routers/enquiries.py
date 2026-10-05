from fastapi import APIRouter

from lib.db import db
from models.enquiry import Enquiry, EnquiryCreate


router = APIRouter(prefix="/enquiries", tags=["enquiries"])


@router.post("", response_model=Enquiry)
async def create_enquiry(input: EnquiryCreate) -> Enquiry:
    enquiry = Enquiry(**input.model_dump())
    await db.enquiries.insert_one(enquiry.model_dump())
    return enquiry


@router.get("", response_model=list[Enquiry])
async def get_enquiries() -> list[Enquiry]:
    records = await db.enquiries.find().sort("created_at", -1).to_list(1000)
    return [Enquiry(**record) for record in records]