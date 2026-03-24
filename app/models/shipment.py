import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import ShipmentStatus
from app.models.status_event import StatusEvent


class Shipment(Base):
    __tablename__ = "shipments"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    tracking_number: Mapped[str] = mapped_column(String(20), unique=True)
    sender_name: Mapped[str] = mapped_column(String(100))
    recipient_name: Mapped[str] = mapped_column(String(100))
    origin: Mapped[str] = mapped_column(String(200))
    destination: Mapped[str] = mapped_column(String(200))
    status: Mapped[ShipmentStatus] = mapped_column(default=ShipmentStatus.pending)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    events: Mapped[list["StatusEvent"]] = relationship(back_populates="shipment")
