"""Example usage of the AI Cognitive Core modules.

此文件显示如何通过 ModuleScheduler 处理用户输入。
"""
from .scheduler import ModuleScheduler

if __name__ == "__main__":
    # Create scheduler which wires up all modules
    scheduler = ModuleScheduler()
    # Process a sample text without audio/video
    result = scheduler.process("今天的天气怎么样？")
    print(result["response"])
    print("Personality:", result["personality"])
