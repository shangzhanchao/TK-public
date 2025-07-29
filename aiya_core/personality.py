class PersonalityGrowthEngine:
    """Simple OCEAN-based personality tracker.

    简单的 OCEAN 人格模型跟踪器，使用五位度来表示 AI 的性格特征。
    """

    def __init__(self, openness=0.5, conscientiousness=0.5,
                 extraversion=0.5, agreeableness=0.5, neuroticism=0.5):
        """Initialize default OCEAN values.

        初始化默认的 OCEAN 特征值，范围为 0-1。
        """
        self.traits = {
            "O": openness,
            "C": conscientiousness,
            "E": extraversion,
            "A": agreeableness,
            "N": neuroticism,
        }

    def update(self, feedback):
        """Update traits based on user feedback.

        `feedback` 应为一个包含 O、C、E、A、N 键的 dict，
        值范围为 [-1, 1]，表示对应程度的增减值。
        """
        for k, v in feedback.items():
            if k in self.traits:
                self.traits[k] = min(1.0, max(0.0, self.traits[k] + v))

    def get_profile(self):
        """Return a copy of current trait values.

        返回当前 OCEAN 特征的复制，可作为客户端使用。
        """
        return self.traits.copy()
