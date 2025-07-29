"""AIYA Cognitive Core package.

This package contains simplified implementations of the modules that make up
the AIYA emotional companion robot backend.
这个包包含了 AIYA 情感陪伴机器人后端的简化实现。
"""

from .personality import PersonalityGrowthEngine
from .memory import SemanticMemorySystem
from .emotion import MultiModalEmotionRecognizer
from .dialogue import GrowthDialogueSystem
from .scheduler import ModuleScheduler

__all__ = [
    "PersonalityGrowthEngine",
    "SemanticMemorySystem",
    "MultiModalEmotionRecognizer",
    "GrowthDialogueSystem",
    "ModuleScheduler",
]

