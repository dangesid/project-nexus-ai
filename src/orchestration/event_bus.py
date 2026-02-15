from typing import Dict, Any, List
import threading
from collections import deque


class EventBus:
    """
    Queue-based in memory event bus.

    Responsibilities:
    - Register agents
    - Publish events ----> Queue Events (changed functionality)
    - notify Interested agents -----> Dispatch events sequentially
    """

    def __init__(self):
        self.subscribers: List[Any] = []   # Stores all agents registered to system.
        self.queue = deque()
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
            self.queue.append(event)

    def start(self):
        """
        Start processing events in FIFO order. 
        """
        while True:
            with self.lock:
                if not self.queue:
                    break
                event = self.queue.popleft()

            # No Lock while calling handlers 
            for agent in self.subscribers:
                if agent.can_handle(event):
                    agent.handle(event)
