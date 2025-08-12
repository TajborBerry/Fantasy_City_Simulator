# agents/story_teller.py
'''
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
'''

# agents/story_teller.py
import json
import time
from pathlib import Path
import openai
from openai import OpenAI
import yaml

class StoryTeller:
    def __init__(self, config_path: str, api_key_path: str):
        # Load config from YAML
        config = yaml.safe_load(Path(config_path).read_text())["story_teller"]
        self.model = config["openai_model"]
        self.temperature = config["temperature"]
        self.max_tokens = config["max_tokens"]

        # Load API key
        openai.api_key = Path(api_key_path).read_text().strip()

    def run(self, city_lore: str) -> dict:
        """Generate a draft NPC origin story based on city lore."""
        prompt = f"""
        You are a fantasy story writer.
        Based on the city description below, create a short origin story for a new NPC.

        City description:
        {city_lore}

        Output your answer as a JSON object with this structure:
        {{
            "story": "short origin story",
            "tags": ["list of personality or role tags"],
            "mentions_items": ["list of magic items mentioned, empty if none"]
        }}
        """

        response_text = self._call_api(prompt)
        return self.extract_json(response_text)

    def _call_api(self, prompt: str) -> str:
        """Call the OpenAI API with simple retry logic."""
        client = OpenAI(api_key=openai.api_key)

        retries = 3
        for attempt in range(retries):
            try:
                response = client.chat.completions.create(
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    messages=[
                        {"role": "system", "content": "You are a helpful fantasy writing assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                return response.choices[0].message.content
            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(1.5 * (attempt + 1))  # backoff
                else:
                    raise e

    @staticmethod
    def extract_json(text: str) -> dict:
        """Extract JSON from model output, even if extra text is present."""
        try:
            start = text.find("{")
            end = text.rfind("}") + 1
            return json.loads(text[start:end])
        except Exception:
            # Fall back to direct parse
            return json.loads(text)


if __name__ == "__main__":
    # Example usage
    storyteller = StoryTeller("config/run_config.yaml", "config/API_key.txt")
    lore = Path("config/city_lore.txt").read_text()
    npc_draft = storyteller.run(lore)
    print(json.dumps(npc_draft, indent=2))
