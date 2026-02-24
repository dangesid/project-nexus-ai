from src.agents.base_agent import BaseAgent
from src.llm.llm_client import LLMClient


class ProfilingAgent(BaseAgent):

    def __init__(self, name, event_bus, memory):
        super().__init__(name, event_bus, memory)
        # FIX 1: Proper instantiation
        self.llm_client = LLMClient()

    def can_handle(self, event):
        return event.event_type == "user_activity_processed"

    def handle(self, event):
        print(f"[{self.name}] Updating user profile...")

        user_id = event.payload.get("user_id")
        item_id = event.payload.get("item_id")
        action = event.payload.get("action")

        # LLM enrichment
        prompt = f"""
        User {user_id} performed {action} on item {item_id}.
        Create a short profile summary describing user's interests.
        """

        profile_summary = self.llm_client.run(prompt)

        profile_data = {
            "user_id": user_id,
            "last_interaction": item_id,
            "action": action,
            "profile_summary": profile_summary,
        }

        # FIX 2: Save to memory
        memory_key = f"user_profile:{user_id}"
        self.memory.save(memory_key, profile_data)

        print(f"[{self.name}] Profile saved in memory under {memory_key}")

        # FIX 3: Emit event
        print(f"[{self.name}] Publishing user_profile_updated event")

        self.publish(
            event_type="user_profile_updated",
            payload=profile_data
        )