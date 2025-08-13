# agents/name_creator.py

from pathlib import Path
from openai import OpenAI
import json
import re
import time
import openai
import yaml

class NameCreator:
    def __init__(self, config_path: str, api_key_path: str):
        config = yaml.safe_load(Path(config_path).read_text())["name_creator"]
        self.model = config["openai_model"]
        self.temperature = config["temperature"]
        self.max_tokens = config["max_tokens"]

        # Load API key
        openai.api_key = Path(api_key_path).read_text().strip()

    def run(self, story_text: str) -> str:
        prompt = (
            "You are a fantasy naming assistant.\n"
            "Given the NPC's backstory, determine if a name is mentioned.\n"
            "- If no name is mentioned: invent a fantasy-style full name based on the mentioned race or background.\n"
            "- If only a single name is mentioned: create a realistic full name.\n"
            "- If a full name already exists: keep it as is.\n"
            "Return ONLY valid JSON like: {\"name\": \"Full Name\"}\n\n"
            f"NPC backstory:\n{story_text}"
        )

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
                            {
                                "role": "system",
                                "content": (
                                    "You are a fantasy naming assistant. "
                                    "Always output valid JSON like {\"name\": \"Full Name\"} "
                                    "with no extra text."
                                )
                            },
                            {"role": "user", "content": prompt}
                        ]
                    )
                    return response.choices[0].message.content
                except Exception as e:
                    if attempt < retries - 1:
                        time.sleep(1.5 * (attempt + 1))  # backoff
                    else:
                        raise e

    def extract_json(self, text: str) -> dict:
        """Extract JSON from text safely."""
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
            else:
                raise ValueError("No valid JSON found in model output.")
