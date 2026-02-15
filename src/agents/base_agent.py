from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    """
This is BaseClass for all agents 

Every Agent must :
1. Define which event type it can handle 
2. Process Incoming Event 
3. Emit new event without directly calling other events 

Agent listens → Receives event → Processes → Emits event    
    """

    def __init__(self, name: str, event_bus):
        """
        Event Bus is A message broker inside our system 
        """
        self.name = name
        self.event_bus = event_bus

    @abstractmethod
    def can_handle(self,event_type: str) -> bool:
        """
        Determine if agent cann handle a specific event type.
        """
        pass

    @abstractmethod
    def handle(self, event: Dict[str, Any]) -> None:
        """
        Process an Incoming event 
        """
        pass

    def publish(self,event: Dict[str, Any]) -> None:
        """
        Publish  a new event to the event bus 
        """
        #this enforces decoupling all the agents depends on event bus, 
        # not each other
        self.event_bus.publish(event) 
             