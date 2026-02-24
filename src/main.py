from src.orchestration.event_bus import EventBus
from src.agents.ingestion_agent.agent import IngestionAgent
from src.agents.profiling_agent.agent import ProfilingAgent
from src.orchestration.event import Event
from src.core.memory_store import MemoryStore
from src.core.graph_store import GraphStore
from src.agents.graph_agent.agent import GraphAgent
from src.agents.recommendation_agent.agent import RecommendationAgent
from src.agents.graph_agent.agent import GraphAgent
from src.llm.llm_client import LLMClient

def main():

    # Infra 

    event_bus = EventBus()
    memory =  MemoryStore()
    graph_store = GraphStore()
    llm_client = LLMClient()

    # Agents 

    ingestionAgent = IngestionAgent(
        name="IngestionAgent",
        event_bus=event_bus,
        memory=memory)
    
    profiling_agent = ProfilingAgent(
        name = "ProfilingAgent",
        event_bus=event_bus,
        memory=memory
    )

    graph_agent = GraphAgent(
        name="GraphAgent",
        event_bus=event_bus,
        memory=memory,
        graph_store=graph_store,
        llm_client=llm_client
    )
    recommendation_agent = RecommendationAgent(
        name= "RecommendationAgent",
        event_bus=event_bus,
        memory=memory,
        graph_store=graph_store,
        llm_client=llm_client
    )

    #Register Agent
    event_bus.register(ingestionAgent)
    event_bus.register(profiling_agent)
    event_bus.register(graph_agent)
    event_bus.register(recommendation_agent)

    #simulate Raw event
    sample_event_payload = {
        "user_id": "U123",
        "item_id": "I456",
        "action": "watched",
        "platform": "netflix",
        "title": "Stranger Things",
        "genre": "Sci-Fi",
    }

    initial_event = Event.create(
        event_type="raw_user_activity",
        payload=sample_event_payload,
        source_agent="system"
    )
    event_bus.publish(initial_event)

    #Start event loop
    event_bus.start()   

if __name__ == "__main__":
    main()