from fastapi import FastAPI

from app.routers.shipment import router as shipment_router

app = FastAPI(title="Delivery Tracker")

app.include_router(shipment_router)


@app.get("/health")
async def health():
    return {"status": "ok"}
