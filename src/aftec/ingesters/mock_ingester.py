import random
import time
from datetime import datetime
from ..core.models import SoilSample

class MockIngester:
    """Generate random but logical data (similar to normal soil)"""
    def __init__(self, sensor_id="mock_sensor_01"):
        self.sensor_id = sensor_id

    def read(self) -> SoilSample:
        # مقادیر معمول: دما 15 تا 30، pH 6 تا 7.5
        temp = round(random.uniform(15, 30), 1)
        ph = round(random.uniform(6.0, 7.5), 1)
        # گاهی ناهنجاری ایجاد می‌کنیم (برای تست)
        if random.random() < 0.05:  # 5% ناهنجاری
            temp = random.choice([-5, 55])
            ph = random.choice([3.0, 10.0])
        return SoilSample(
            sensor_id=self.sensor_id,
            temperature_c=temp,
            ph=ph,
            timestamp=datetime.now()
        )
