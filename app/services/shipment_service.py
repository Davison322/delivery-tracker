import random
import string
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.shipment import Shipment
from app.schemas.shipment import ShipmentCreate


class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_shipment(self, data: ShipmentCreate) -> Shipment:
        tracking_number = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=12)
        )
        shipment = Shipment(
            tracking_number=tracking_number,
            sender_name=data.sender_name,
            recipient_name=data.recipient_name,
            origin=data.origin,
            destination=data.destination,
        )
        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)
        return shipment

    async def get_shipment(self, shipment_id: uuid.UUID) -> Shipment | None:
        result = await self.session.execute(
            select(Shipment).where(Shipment.id == shipment_id)
        )
        return result.scalar_one_or_none()
