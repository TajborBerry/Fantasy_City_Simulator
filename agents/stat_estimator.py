# agents/stat_estimator.py
class StatEstimator:
    def __init__(self, model, temperature, max_tokens, stat_range):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.stat_min = stat_range["min"]
        self.stat_max = stat_range["max"]

    def run(self, story):
        # For now, return fixed example stats
        return {
            "Strength": 12,
            "Dexterity": 14,
            "Constitution": 13,
            "Intelligence": 10,
            "Wisdom": 11,
            "Charisma": 15
        }
