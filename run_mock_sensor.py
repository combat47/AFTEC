import sys
import time
sys.path.insert(0, 'src')  # برای دسترسی به ماژول aftec

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
