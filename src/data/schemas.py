from pydantic import BaseModel
from typing import Any, Dict
import datetime
import uuid

class Event(BaseModel):
    event_id: str
    event_type: str
    payload: Dict[str, Any]
    source_agent: str
    timestamp: datetime.datetime

    @staticmethod
    def create(event_type: str, payload: Dict[str, Any], source_agent: str):
        return Event(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            payload=payload,
            source_agent=source_agent,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
        )