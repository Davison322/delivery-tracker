# Delivery Tracker

Simple backend for tracking shipments and their status history.

## What it does

* **Shipment management** – Create and view shipments.
* **Status history** – Each shipment has a list of events (like "picked up" or "delivered").
* **Timezones** – Saves everything in UTC to avoid time mess.
* **Validation** – Checks if input data is correct before saving to DB.

## Tech Stack

* **Python** (FastAPI)
* **PostgreSQL** (Database)
* **SQLAlchemy** (ORM)
* **Alembic** (Migrations)
* **uv** (Package manager)
* **Docker** (to run DB)

## Project Structure
```text
app/
├── db/              # DB connection
├── models/          # Database tables
├── routers/         # API endpoints
├── schemas/         # Data validation
├── services/        # Logic
└── main.py          # App entry point
```

## Future Plans (Roadmap)
* [ ] **Tests** – Add integration tests with `pytest`
* [ ] **Background Tasks** – Auto-update statuses after a delay (simulating real logistics).
* [ ] **History API** – Add endpoints to manually update a shipment's history.
* [ ] **Search & Filter** – Search shipments by tracking number or status.

## How to Run

1.  **Start the database:**
    ```bash
    docker-compose up -d
    ```

2.  **Setup environment:**
    ```bash
    uv sync
    ```

3.  **Apply migrations:**
    ```bash
    uv run alembic upgrade head
    ```

4.  **Run the application:**
    ```bash
    uv run uvicorn app.main:app --reload
    ```

## API Documentation

Once the app is running, you can find the interactive Swagger UI at:
`http://127.0.0.1:8000/docs`

## API Example

**Create a shipment:**
```bash
curl -X POST http://localhost:8000/shipments \
  -H "Content-Type: application/json" \
  -d '{
    "sender_name": "Vitalii Papich",
    "recipient_name": "Pavlo Streamsniper",
    "origin": "Vinnytsia",
    "destination": "Lviv"
  }'
```

**Response:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "tracking_number": "UZXICCIRCJ5T",
  "sender_name": "Vitalii Papich",
  "recipient_name": "Pavlo Streamsniper",
  "origin": "Vinnytsia",
  "destination": "Lviv",
  "status": "pending",
  "created_at": "2026-03-24T16:07:00Z"
}
```
