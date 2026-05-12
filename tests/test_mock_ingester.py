import pytest
from aftec.ingesters.mock_ingester import MockIngester
from aftec.core.models import SoilSample

def test_mock_ingester_returns_valid_sample():
    ingester = MockIngester(sensor_id="test")
    sample = ingester.read()
    assert isinstance(sample, SoilSample)
    assert sample.sensor_id == "test"
    assert -10 <= sample.temperature_c <= 60
    assert 0 <= sample.ph <= 14
    assert sample.timestamp is not None

def test_mock_ingester_randomness():
    ingester = MockIngester()
    samples = [ingester.read() for _ in range(10)]
    temps = [s.temperature_c for s in samples]
    phs = [s.ph for s in samples]
    # Should not be all identical (though could be by chance, so just check range)
    assert any(t != temps[0] for t in temps) or any(p != phs[0] for p in phs)
