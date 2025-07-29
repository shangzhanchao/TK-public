"""Demo of PersonalityGrowthEngine.
性格生长引擎示例
"""
from aiya_core.personality import PersonalityGrowthEngine

if __name__ == "__main__":
    engine = PersonalityGrowthEngine()
    print("Initial:", engine.get_profile())
    # Update personality traits based on hypothetical user feedback
    # 根据例何的用户反馈更新性格
    engine.update({"O": 0.1, "E": -0.1})
    print("Updated:", engine.get_profile())
