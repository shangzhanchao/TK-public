"""Demo of SemanticMemorySystem.
语义记忆系统示例
"""
from aiya_core.memory import SemanticMemorySystem

if __name__ == "__main__":
    memory = SemanticMemorySystem()
    memory.store("hello")
    memory.store("hi again", tag="greet")
    print("Recent:", memory.recent())
    print("Search 'hi':", memory.retrieve("hi"))
