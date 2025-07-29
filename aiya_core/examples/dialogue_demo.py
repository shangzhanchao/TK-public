"""Demo of GrowthDialogueSystem.
生长式对话系统示例
"""
from aiya_core.personality import PersonalityGrowthEngine
from aiya_core.memory import SemanticMemorySystem
from aiya_core.dialogue import GrowthDialogueSystem

if __name__ == "__main__":
    personality = PersonalityGrowthEngine()
    memory = SemanticMemorySystem()
    dialogue = GrowthDialogueSystem(personality, memory)
    reply = dialogue.generate_response("今天还好吗？")
    print("Reply:", reply)
    print("Memory:", memory.recent())
