from src.orchestration.event_bus import EventBus
from src.agents.ingestion_agent.agent import IngestionAgent
from src.agents.profiling_agent.agent import ProfilingAgent
from src.data.schemas import Event
from src.core.memory_store import MemoryStore

def main():
    event_bus = EventBus()
    memory =  MemoryStore()

    ingestionAgent = IngestionAgent(
        name="IngestionAgent",
        event_bus=event_bus,
        memory=memory)
    
    profiling_agent = ProfilingAgent(
        name = "ProfilingAgent",
        event_bus=event_bus,
        memory=memory
    )

    #Register Agent
    event_bus.register(ingestionAgent)
    event_bus.register(profiling_agent)

    #simulate Raw event
    initial_event = Event.create(
        event_type="raw_data_received",
        payload={
            "user_id": "U123",
            "item_id": "I456",
            "action": "watched"
        },
        source_agent="system"
    )
    # change it to queue based structure
    event_bus.publish(initial_event)
    event_bus.start()   # added this function

if __name__ == "__main__":
    main()