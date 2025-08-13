# main.py
import yaml
from pathlib import Path
import datetime
import json

# Import your agents
from agents import StoryTeller, StatEstimator, NameCreator

# --- 1) Load config and API key ---
CONFIG_PATH = Path("config/run_config.yaml")
API_KEY_PATH = Path("config/API_key.txt")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

with open(API_KEY_PATH, "r") as f:
    api_key = f.read().strip()

# (Set up OpenAI API client)
import openai
openai.api_key = api_key

# --- 2) Load static city lore ---
CITY_LORE_PATH = Path(config["city_lore_file"])
city_lore = CITY_LORE_PATH.read_text()

# --- 3) Run agents based on config ---
npc_data = {}

# If want to use test environemnt to save on time and tokens.
if config.get("use_mock_data"):
    npc_data.update(json.loads(Path(config["mock_data_file"]).read_text()))


if config["agents"]["story_teller"]:
    storyteller = StoryTeller(CONFIG_PATH, API_KEY_PATH)
    npc_data["story"] = storyteller.run(city_lore)


if config["agents"]["stat_estimator"]:
    stat_estimator = StatEstimator(model=config["openai_model"],
                                   temperature=config["temperature"],
                                   max_tokens=config["max_tokens"],
                                   stat_range=config["stat_range"])
    npc_data["stats"] = stat_estimator.run(npc_data.get("story", ""))

if config["agents"]["name_creator"]:
    name_creator = NameCreator(CONFIG_PATH, API_KEY_PATH)
    npc_data["name"] = name_creator.run(npc_data.get("story", ""))

# --- 4) Save output ---
if config["save_outputs"]:
    output_folder = Path(config["output_folder"])
    output_folder.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_folder / f"npc_{timestamp}.json"
    with open(output_file, "w") as f:
        json.dump(npc_data, f, indent=2)

print("NPC generated:", npc_data)
