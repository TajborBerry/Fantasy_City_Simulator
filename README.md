# 🏙️ Fantasy City NPC Generator

An AI-powered tool to generate richly detailed, D&D-style NPCs (Non-Player Characters) based on a fantasy city's lore — using OpenAI's API and a modular, agent-based architecture.

## ✨ What It Does

Given a city's background story, this project generates fully fleshed-out NPCs with:

- 🎭 Personal origin stories  
- 📊 D&D-style stats (STR, DEX, etc.)  
- 🧝 Character names  
- 🪄 Magic item descriptions (if applicable)  
- 🧬 Family backstories (optional)  
- 🗺️ Fun facts and tales (optional)  

All of this is handled by dedicated agents and coordinated through a simple configuration.

---

## 🧠 Agent Architecture

Each agent is responsible for a specific piece of the NPC generation process:

| Agent Name           | Responsibility                                                  |
|----------------------|-----------------------------------------------------------------|
| `StoryTeller`        | Drafts the NPC’s origin story based on the city lore            |
| `StatEstimator`      | Estimates D&D stats based on the story                          |
| `NameCreator`        | Generates a fitting name                                        |
| `ItemCreator`        | Describes any magic item mentioned in the story (optional)      |
| `FinalStoryCreator`  | Finalizes the story with refined details and item integration   |
| `TalesTeller`        | Adds an interesting fact or tale about the NPC (optional)       |
| `FamilyHistory`      | Provides a short backstory of the NPC’s family (optional)       |

The orchestrator reads `run_config.yaml` to control which agents are used and in what order.

---

## 🗂️ Folder Structure

```
Fantasy_City_Simulator/
│
├── agents/                # Modular agents (each one in its own file)
│├── __init__.py           # Clean re-exports for easy importing
│├── story_teller.py
│├── stat_estimator.py
│├── name_creator.py
│├── ...
│
├── config/
│├── API_key.txt           # Your OpenAI API key (not tracked in Git)
│├── run_config.yaml       # Controls which agents run and their parameters
│
├── output/                # Generated NPCs (ignored in .gitignore)
│
├── tests/                 # Fixtures, test NPCs, and testing utils
│
├── main.py                # Main orchestrator script
└── README.md              # You're reading it!
```

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/fantasy-city-npc-generator.git
   cd fantasy-city-npc-generator
   ```

2. **Install dependencies**  
   (You’ll need Python 3.10+ and `openai`)
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your config**  
   - Add your OpenAI key to `config/API_key.txt`  
   - Edit `config/run_config.yaml` to choose which agents to use

4. **Run the orchestrator**  
   ```bash
   python main.py
   ```

---

## 🛠️ Features Planned

- 🧠 Memory-aware NPCs with consistent personalities  
- 🗃️ Curated NPC database with search/filter support  
- 🎲 Integration with virtual tabletops (Foundry, Roll20)  
- 🌍 Procedural generation of cities, factions, and quests  

---

## 🙌 Credits

Created by [Your Name] — inspired by modular AI design, worldbuilding, and the love of storytelling through code.

---

## ⚠️ Disclaimer

This project uses the OpenAI API and may incur costs depending on your usage. Use your API key responsibly.
