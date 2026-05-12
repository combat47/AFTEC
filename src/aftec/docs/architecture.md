# AFTEC Architecture Overview

AFTEC is a modular, event‑driven system for monitoring soil parameters (temperature, pH) and detecting anomalies. It is designed to be extended with new sensors, storage backends, and AI models without changing core logic.

## High‑level components
```text
[Sensor Hardware] → [Ingester] → [Pipeline] → [Storage] → [Monitoring/Alerting]
↓ ↓
[Anomaly Detector] [Dashboard/API]
```

## Layer description

### 1. Ingesters (`src/aftec/ingesters/`)
- Read data from different sources: mock (for testing), serial (USB), MQTT, file, etc.
- Implement `BaseIngester` (abstract class).
- Output: `SoilSample` object (validated with Pydantic).

### 2. Core models (`src/aftec/core/models.py`)
- `SoilSample`: sensor_id, temperature_c, ph, timestamp.
- Validation: temperature (-10…60°C), pH (0…14).

### 3. Storage (`src/aftec/storage/`)
- Persist samples to databases.
- `BaseStorage` interface: `save(sample)`, `get_recent(limit)`, etc.
- Current implementation: SQLite. Future: PostgreSQL, InfluxDB (time‑series).

### 4. Anomaly Detectors (`src/aftec/detectors/`)
- `BaseDetector` with method `is_anomaly(sample, history)`.
- IQR detector (simple statistical method).
- Future: Isolation Forest, LSTM autoencoder.

### 5. Monitoring (`src/aftec/monitoring/`)
- `dashboard.py` – Streamlit UI showing live charts, anomaly highlights.
- `notifier.py` – send Telegram alerts when anomalies occur.

## Data flow (typical)

1. Ingester reads a new `SoilSample` (every 2 seconds by default).
2. The main pipeline (`scripts/run_ingester.py`) receives the sample.
3. Anomaly detector checks against recent history (window of last 100 samples).
4. Sample is saved to database (SQLite).
5. If anomaly: a log is written and (future) an alert is sent.
6. Dashboard queries the database every few seconds and updates plots.

## Directory structure reminder
```text
src/aftec/
├── core/ # models & base classes
├── ingesters/ # data sources
├── storage/ # database backends
├── detectors/ # anomaly detection algorithms
├── monitoring/ # UI & notifications
└── scripts/ # runnable entry points
```

## Design principles

- **Open/Closed**: New ingesters/detectors/storages can be added without modifying existing ones.
- **Dependency injection**: The main script decides which components to use.
- **Testability**: Each component can be unit‑tested with mocks.
- **Configuration via environment variables** (`.env` file) for secrets (DB paths, tokens).

## Future extensions

- Real‑time streaming with Kafka
- Predictive models (forecasting temp/pH)
- REST API (FastAPI) for remote access
- Containerization (Docker) for easy deployment
