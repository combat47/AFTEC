#!/usr/bin/env python3
"""Main ingester script – reads from sensor, stores, detects anomalies."""

import sys
import time
from pathlib import Path

# Add project root to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from aftec.ingesters.mock_ingester import MockIngester  # noqa: E402


def main():
    """Run the main ingester loop."""
    print("AFTEC Ingester starting...")
    ingester = MockIngester()

    try:
        while True:
            sample = ingester.read()
            print(
                f"[{sample.timestamp}] {sample.sensor_id} | "
                f"temp={sample.temperature_c}°C pH={sample.ph}"
            )
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nIngester stopped.")


if __name__ == "__main__":
    main()
