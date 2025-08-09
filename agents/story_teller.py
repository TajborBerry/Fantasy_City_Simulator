# agents/story_teller.py
class StoryTeller:
    def __init__(self, model, temperature, max_tokens):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def run(self, city_lore):
        # For now, just return a fake story to test the flow
        return (
            "Born in the bustling harbor district, our NPC grew up watching "
            "ships arrive from distant lands. They learned early how to "
            "negotiate and survive in a city that prized hard work."
        )
