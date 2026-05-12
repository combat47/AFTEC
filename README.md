<div align="center">
  <h1>🌱 AFTEC – Ai Farming TECHnology</h1>
  <p><strong>Because your soil deserves a brain 🧠 + 🤖</strong></p>
  <p>
    <a href="https://github.com/combat47/AFTEC/edit/main/README.md#-quick-start-do-it-in-2-minutes">Quick Start</a> •
    <a href="https://github.com/combat47/AFTEC/blob/main/README.md#-modular-architecture-like-pokad-but-farming">Architecture</a> •
    <a href="https://github.com/combat47/AFTEC/blob/main/README.md#%EF%B8%8F-roadmap-transparent-no-bullshit">Roadmap</a> •
    <a href="https://github.com/combat47/AFTEC/blob/main/README.md#-contributing-yes-you"-contributing">Contributing</a> •
    <a href="https://github.com/combat47/AFTEC/blob/main/README.md#-license">License</a>
  </p>
</div>

AFTEC is a **modular**, **open‑source** AI platform for precision farming.  
It starts simple: monitor **soil temperature** and **pH** from sensors, detect anomalies, and later predict trends – all while staying clean and expandable.

Think of it as POKAD but for agriculture. 🏡→🌾

---

## 🎯 Why AFTEC?

- **For developers** – clean interfaces (`BaseIngester`, `BaseStorage`, `BaseDetector`), easy to extend with MQTT, LoRa, or new ML models.  
- **For farmers** – catches weird readings before crops suffer, sends alerts, and visualizes data.  
- **For your resume** – shows you can build production‑ready, testable, containerized AI systems.  
- **For business** – you can later offer a SaaS version or custom hardware integration.

> 💡 **Still early?** Yes – and that's good. We build step‑by‑step, no spaghetti.

---

## 🧱 Modular Architecture (like POKAD, but farming)
```text
AFTEC/
├── src/aftec/
│ ├── core/ # data models & abstract base classes
│ ├── ingesters/ # read from serial, mock, MQTT, etc.
│ ├── storage/ # SQLite (now), PostgreSQL/InfluxDB (later)
│ ├── detectors/ # anomaly detection (IQR → IsolationForest → LSTM)
│ └── monitoring/ # dashboard (Streamlit) + notifiers (Telegram)
├── scripts/ # run mock sensor, run ingester
├── tests/ # pytest unit tests
└── docs/ # detailed docs (mkdocs later)
```

**Current scope (MVP):**  
- Mock sensor (generates realistic temp/pH with occasional anomalies)  
- SQLite storage  
- IQR‑based anomaly detector  
- Simple CLI dashboard (or Streamlit)  
- Full test suite  

**Later:**  
- Real sensor support (USB serial / Modbus)  
- Predictive model (ARIMA or tiny LSTM)  
- Telegram alerts  
- Docker & cloud deploy  

---

## 🚀 Quick Start (do it in 2 minutes)

```bash
git clone https://github.com/combat47/AFTEC.git
cd AFTEC
make install
make run-sim
```
In another terminal:

```bash
make run-ingester
```
🎉 You'll see mocked sensor data being ingested and saved to aftec.db.
Anomalies (e.g., pH 3.0 or temp 55°C) will be flagged.

🛠️ Makefile commands (save your brain)

| Command	| What it does |
|---------|---------|
| make install	| install deps + package in editable mode |
| make run-sim	| run mock sensor (prints fake data) |
| make run-ingester	| main loop: read from mock sensor → store → detect anomalies |
| make test	| run all tests with pytest |
| make clean	| remove cache files |

## 🧪 Example output (ingester)
```text
[2025-05-12 14:32:01] sensor=mock_01 | temp=22.3°C | pH=6.8 | anomaly=False
[2025-05-12 14:32:03] sensor=mock_01 | temp=23.1°C | pH=7.0 | anomaly=False
[2025-05-12 14:32:05] sensor=mock_01 | temp=55.0°C | pH=3.2 | anomaly=True ⚠️
```
Anomaly detection currently uses IQR on a sliding window of last 100 readings.
Simple, explainable, and easy to replace later.

## 🗺️ Roadmap (transparent, no bullshit)
Phase 0 – Project structure, mock sensor, base classes

Phase 1 – SQLite storage + IQR anomaly detector + unit tests

Phase 2 – Streamlit dashboard (live plots, anomaly highlights)

Phase 3 – Telegram notifier (get alerts when soil goes crazy)

Phase 4 – Real serial sensor integration (Arduino + pH probe + DS18B20)

Phase 5 – Predictive model (forecast temp/pH for next 6h)

Phase 6 – Docker + docker‑compose, cloud deployment template

Each phase is a separate milestone with its own branch and release.

## 🤝 Contributing (yes, you!)
You want to help? Awesome.

Fork, create a feature branch, open a PR.

Keep the modular spirit – new ingesters, detectors, or storage backends are welcome.

Write tests (pytest) for anything non‑trivial.

Use make test before pushing.

We also welcome real‑world sensor configs (e.g., how to connect a specific pH meter).
Share your setup in docs/hardware/.

## 💰 Monetization? (because open source should not mean starving)
This repo is MIT licensed – free forever.
But if you want to make money:

SaaS version – hosted dashboard, multi‑farm, premium alerts.

Consulting – help farms integrate AFTEC with their existing sensors.

White‑label – sell a branded version to agritech companies.

All using the same core code. I'll keep the core open, you build business on top.

## 📄 License
Apache 2.0 © [Amirhossein Jahazi] – do whatever you want, but keep the original copyright, disclaimer, and note any changes.

## ⭐ Show your support
If AFTEC helps you or makes you smile, star this repo 🌟 and share it with a farmer or a dev friend.

Made with ☕, Python, and a dream of smarter fields.
