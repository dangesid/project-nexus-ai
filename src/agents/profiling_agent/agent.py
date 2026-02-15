from src.agents.base_agent import BaseAgent

class ProfilingAgent(BaseAgent):
    
    def can_handle(self, event):
        return event.event_type == "user_activity_processed"

    def handle(self, event):
        if event.event_type == "user_activity_processed":
            print(f"[{self.name}] Updating user profile ...")

            user_id = event.payload.get("user_id")
            item_id = event.payload.get("item_id")
            action = event.payload.get("action")

            profile_data = {
                "user_id" : user_id,
                "last_interaction": item_id,
                "action" : action,
                "profile_strength": "intermediate"
            }

            print(f"[{self.name}] Publising user profile updated event")
            
            self.publish(
                event_type="user_profile_updated",
                payload=profile_data
            )
