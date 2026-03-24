import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.enums import ShipmentStatus


import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.enums import ShipmentStatus


class ShipmentCreate(BaseModel):
    sender_name: str
    recipient_name: str
    origin: str
    destination: str


class ShipmentResponse(BaseModel):
    id: uuid.UUID
    tracking_number: str
    sender_name: str
    recipient_name: str
    origin: str
    destination: str
    status: ShipmentStatus
    created_at: datetime

    model_config = {"from_attributes": True}