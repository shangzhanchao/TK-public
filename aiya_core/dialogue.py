class GrowthDialogueSystem:
    """Generates responses using personality and memory.

    使用性格和记忆信息来生成对应话答，例子通过简单的规则解析。
    """

    def __init__(self, personality_engine, memory_system):
        """Connect personality and memory modules."""
        self.personality = personality_engine
        self.memory = memory_system

    def generate_response(self, user_input, emotions=None):
        """Very simple rule-based response generator.

        在实际的系统中，这里可以调用大型语言模型来生成回复。
        """
        # Use current personality profile to influence the reply
        profile = self.personality.get_profile()
        # Record user input in memory
        self.memory.store(user_input, emotions=emotions, role="user")
        # Compose a simple response containing openness trait
        response = f"[O:{profile['O']:.2f}] 我收到你的消息: {user_input}"
        self.memory.store(response, role="assistant")
        return response
