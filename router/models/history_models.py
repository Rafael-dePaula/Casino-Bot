from datetime import datetime
from pydantic import BaseModel


class RouletteModel(BaseModel):
    number: int
    time: datetime


