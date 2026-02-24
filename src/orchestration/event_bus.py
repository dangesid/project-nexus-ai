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
            print(f"[Event Bus] Registered agent: {agent.name}")
    
    def publish(self, event: Dict[str,Any]):
        """
        Publish an event to all interested agents.
        """
        with self.lock:
            print(f"[EventBus] Event published → {event.event_type}")
            self.queue.append(event)

    def start(self):
        """
        Start processing events in FIFO order. 
        """
        print("[EventBus] Starting event loop")
        while True:
            with self.lock:
                if not self.queue:
                    print("[EventBus] Queue empty → stopping")
                    break
                event = self.queue.popleft()
                print(f"[EventBus] Dispatching → {event.event_type}")

            # No Lock while calling handlers 
            for agent in self.subscribers:
                if agent.can_handle(event):
                    print(f"[EventBus] → {agent.name} handling")
                    agent.handle(event)
