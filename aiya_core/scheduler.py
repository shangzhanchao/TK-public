from .personality import PersonalityGrowthEngine
from .memory import SemanticMemorySystem
from .emotion import MultiModalEmotionRecognizer
from .dialogue import GrowthDialogueSystem


class ModuleScheduler:
    """Coordinates the sub modules for processing user interaction.

    组织各子模块的调用，引导用户交互的数据流程。
    """

    def __init__(self):
        """Initialize all sub modules."""
        self.personality = PersonalityGrowthEngine()
        self.memory = SemanticMemorySystem()
        self.emotion = MultiModalEmotionRecognizer()
        self.dialogue = GrowthDialogueSystem(self.personality, self.memory)

    def process(self, text, audio=None, video=None):
        """Process user input and return structured result."""
        # Recognize emotion from audio or video (placeholder)
        emotions = self.emotion.analyze(audio_path=audio, video_path=video)
        # Here we could update personality based on emotions
        response = self.dialogue.generate_response(text, emotions=emotions)
        return {
            "response": response,
            "personality": self.personality.get_profile(),
            "emotions": emotions,
            "memory_recent": self.memory.recent(),
        }
