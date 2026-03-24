from enum import Enum


class ShipmentStatus(str, Enum):
    pending = "pending"
    picked_up = "picked_up"
    in_transit = "in_transit"
    delivered = "delivered"
