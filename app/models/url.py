from datetime import datetime

from pydantic import BaseModel


class Url(BaseModel):
    name: str
    type: str
    createdAt: datetime
