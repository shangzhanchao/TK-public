from .personality_growth import PersonalityGrowthEngine
from .semantic_memory import SemanticMemorySystem
from .emotion_recognition import MultiModalEmotionRecognizer
from .dialogue_system import GrowthDialogueSystem


class ModuleScheduler:
    """Coordinates the sub modules for processing user interaction."""

    def __init__(self):
        self.personality = PersonalityGrowthEngine()
        self.memory = SemanticMemorySystem()
        self.emotion = MultiModalEmotionRecognizer()
        self.dialogue = GrowthDialogueSystem(self.personality, self.memory)

    def process(self, text, audio=None, video=None):
        emotions = self.emotion.analyze(audio_path=audio, video_path=video)
        # personality update logic would go here using emotions or other cues
        response = self.dialogue.generate_response(text, emotions=emotions)
        return {
            "response": response,
            "personality": self.personality.get_profile(),
            "emotions": emotions,
            "memory_recent": self.memory.recent(),
        }
