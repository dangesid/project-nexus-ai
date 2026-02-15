from src.orchestration.event_bus import EventBus
from src.agents.ingestion_agent.agent import IngestionAgent

def main():
    event_bus = EventBus()

    ingestionAgent = IngestionAgent(name="IngestionAgent", event_bus=event_bus)

    #Register Agent
    event_bus.register(ingestionAgent)

    #simulate Raw event
    event_bus.publish({
        "event_type": "raw_data_received",
        "payload":{
            "user_id": "U123",
            "item_id": "I456",
            "action": "watched"
        }
    })

if __name__ == "__main__":
    main()