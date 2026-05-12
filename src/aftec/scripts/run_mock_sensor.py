#!/usr/bin/env python3
"""Mock sensor simulator – generates fake temp/pH readings."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from aftec.ingesters.mock_ingester import MockIngester

def main():
    ingester = MockIngester()
    print("Mock Sensor Running (Ctrl+C to stop)")
    while True:
        sample = ingester.read()
        print(f"[{sample.timestamp}] Temp:{sample.temperature_c}°C  pH:{sample.ph}")
        time.sleep(2)

if __name__ == "__main__":
    main()
