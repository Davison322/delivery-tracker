import uuid
from datetime import datetime, timezone

from sqlalchemy import (DateTime, ForeignKey, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.enums import ShipmentStatus


class StatusEvent(Base):
    __tablename__ = "status_events"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    shipment_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("shipments.id"))
    status: Mapped[ShipmentStatus]
    location: Mapped[str] = mapped_column(String(200))
    note: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    shipment: Mapped["Shipment"] = relationship(back_populates="events")