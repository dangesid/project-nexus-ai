from typing import Dict, Any, List
import threading

class EventBus:
    """
    Simple in memory event bus.

    Responsibilities:
    - Register agents
    - Publish events
    - notify Interested agents 
    """

    def __init__(self):
        self.subscribers: List[Any] = []   # Stores all agents registered to system.
        self.lock = threading.RLock()
        

    def register(self,agent):
        """
        Register an agent to listen for events.
        """
        with self.lock:
            self.subscribers.append(agent)
    
    def publish(self, event: Dict[str,Any]):
        """
        Publish an event to all interested agents.
        """
        with self.lock:
            for agent in self.subscribers:
                if agent.can_handle(event):
                    agent.handle(event)
