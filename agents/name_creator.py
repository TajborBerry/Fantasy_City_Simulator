# agents/name_creator.py
class NameCreator:
    def __init__(self, model, temperature, max_tokens):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def run(self, story, stats):
        # For now, just return a static name
        return "Lira Windharbor"
