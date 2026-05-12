#!/usr/bin/env python3
"""Main ingester script – reads from sensor, stores, detects anomalies."""

import sys
import time
from pathlib import Path

# Add project root to path if needed (for development)
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from aftec.ingesters.mock_ingester import MockIngester
# from aftec.storage.sqlite_storage import SQLiteStorage
# from aftec.detectors.iqr_detector import IQRDetector

def main():
    print("AFTEC Ingester starting...")
    ingester = MockIngester()
    # storage = SQLiteStorage("aftec.db")
    # detector = IQRDetector(window_size=100)

    try:
        while True:
            sample = ingester.read()
            # TODO: store and detect anomaly
            print(f"[{sample.timestamp}] {sample.sensor_id} | temp={sample.temperature_c}°C pH={sample.ph}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nIngester stopped.")

if __name__ == "__main__":
    main()
