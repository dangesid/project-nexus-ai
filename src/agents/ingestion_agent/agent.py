from typing import Dict, Any
from src.agents.base_agent import BaseAgent
from src.data.schemas import Event

class IngestionAgent(BaseAgent):
    """
    Handles Raw data ingestion

    Responsibilities:
    - Process incoming raw data events
    - Save processed data to MemoryStore
    - Publish new events to the EventBus
    """
    
    def __init__(self, name, event_bus, memory):
        super().__init__(name, event_bus,memory)


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
        # save processed data to memory
        memory_key = f"user_activit:{processing_data['user_id']}"
        self.memory.save(memory_key, processing_data)
        print(f"[{self.name}] Saved process data to memoryStore under key; {memory_key}")


        print(f"[{self.name}] Publishing processed data event")

        self.publish(
            event_type="user_activity_processed",
            payload=processing_data
        )