from datetime import datetime
from pydantic import BaseModel, Field


class SoilSample(BaseModel):
    sensor_id: str
    temperature_c: float = Field(..., ge=-10, le=60)
    ph: float = Field(..., ge=0, le=14)
    timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
