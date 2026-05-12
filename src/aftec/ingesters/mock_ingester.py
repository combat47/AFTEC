import random
from datetime import datetime

from ..core.models import SoilSample


class MockIngester:
    """Generate realistic random soil data (temp 15-30°C, pH 6.0-7.5) with occasional anomalies."""

    def __init__(self, sensor_id="mock_sensor_01"):
        self.sensor_id = sensor_id

    def read(self) -> SoilSample:
        temp = round(random.uniform(15, 30), 1)
        ph = round(random.uniform(6.0, 7.5), 1)
        # 5% chance of anomaly
        if random.random() < 0.05:
            temp = random.choice([-5, 55])
            ph = random.choice([3.0, 10.0])
        return SoilSample(
            sensor_id=self.sensor_id,
            temperature_c=temp,
            ph=ph,
            timestamp=datetime.now()
        )
