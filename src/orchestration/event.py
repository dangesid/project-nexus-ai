class Event:
    """
    Core event object flowing across agents.

    This is the message envelope in the agentic system.

    Contains :
    - event_type -> routing signal 
    - payload -> actual data
    - source agent -> who generated it 
    """

    def __init__(self, event_type: str, payload: dict, source_agent: str = "system"):
        self.event_type = event_type
        self.payload = payload
        self.source_agent = source_agent

    @classmethod
    def create(cls, event_type: str, payload: dict, source_agent: str):
        return cls(event_type, payload, source_agent)
    
    def __repr__(self):
        return f"Event(type={self.event_type}, source={self.source_agent})"
    