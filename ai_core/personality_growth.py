class PersonalityGrowthEngine:
    """Simple OCEAN-based personality tracker."""

    def __init__(self, openness=0.5, conscientiousness=0.5,
                 extraversion=0.5, agreeableness=0.5, neuroticism=0.5):
        self.traits = {
            "O": openness,
            "C": conscientiousness,
            "E": extraversion,
            "A": agreeableness,
            "N": neuroticism,
        }

    def update(self, feedback):
        """Update traits based on user feedback.
        `feedback` should be a dict with keys matching O, C, E, A, N.
        Values are deltas in range [-1, 1]."""
        for k, v in feedback.items():
            if k in self.traits:
                self.traits[k] = min(1.0, max(0.0, self.traits[k] + v))

    def get_profile(self):
        return self.traits.copy()
