"""Example usage of the AI Cognitive Core modules."""
from .module_scheduler import ModuleScheduler

if __name__ == "__main__":
    scheduler = ModuleScheduler()
    result = scheduler.process("你好，今天的天气怎么样？")
    print(result["response"])
    print("Personality:", result["personality"])
