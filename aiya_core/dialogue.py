class GrowthDialogueSystem:
    """Generates responses using personality and memory."""

    def __init__(self, personality_engine, memory_system):
        self.personality = personality_engine
        self.memory = memory_system

    def generate_response(self, user_input, emotions=None):
        """Very simple rule-based response generator."""
        # In a full system this would call an LLM or other model.
        profile = self.personality.get_profile()
        self.memory.store(user_input, emotions=emotions, role="user")
        response = f"[O:{profile['O']:.2f}] 我收到你的消息: {user_input}"
        self.memory.store(response, role="assistant")
        return response
