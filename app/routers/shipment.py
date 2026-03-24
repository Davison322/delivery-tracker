import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import AsyncSessionLocal
from app.schemas.shipment import ShipmentCreate, ShipmentResponse
from app.services.shipment_service import ShipmentService

router = APIRouter(prefix="/shipments", tags=["shipments"])


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=ShipmentResponse, status_code=201)
async def create_shipment(
    data: ShipmentCreate,
    session: AsyncSession = Depends(get_session),
):
    service = ShipmentService(session)
    return await service.create_shipment(data)


@router.get("/{shipment_id}", response_model=ShipmentResponse)
async def get_shipment(
    shipment_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
):
    service = ShipmentService(session)
    shipment = await service.get_shipment(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment
