from typing import Dict, Any
from src.agents.base_agent import BaseAgent
from src.data.schemas import Event

class IngestionAgent(BaseAgent):
    """
    Handles Raw data ingestion
    """

    def can_handle(self, event: str) -> bool:
        return event.event_type == "raw_data_received"

    def handle(self, event: Event) -> None:
        print(f"[{self.name}] Processing raw data...")

        raw_payload = event.payload

        processing_data = {
            "user_id": raw_payload.get("user_id"),
            "item_id": raw_payload.get("item_id"),
            "action": raw_payload.get("action"),
        }
        print(f"[{self.name}] Publishing processed data event")

        self.publish(
            event_type="user_activity_processed",
            payload=processing_data
        )