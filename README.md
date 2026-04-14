# SQL Murder Mystery Agent

An AI agent that autonomously solves the [SQL Murder Mystery](https://mystery.knightlab.com/) using LangChain and Claude. The agent explores the database, follows clues, and identifies the murderer — without being told how.

## How it works

The agent receives a single prompt describing the crime and has access to one tool: `sql_query`. It decides which queries to run, analyzes the results, and reasons through the evidence until it reaches a conclusion.

This is an example of a **dynamic agent** — it chooses its actions at runtime based on what it finds in the data, not a fixed script.

## Stack

- Python 3.13
- LangChain
- Claude Haiku 4.5 (Anthropic)
- SQLite
- uv (package manager)

## Project structure

```
sql_murder_mistery_agent/
├── database/
│   └── sql-murder-mystery.db
├── main.py
├── .env
├── pyproject.toml
└── README.md
```
## Run it yourself

1. Clone the repo:
```bash
git clone https://github.com/sofiasanchezrodrp-sketch/sql_murder_mistery_agent.git
cd sql_murder_mistery_agent
```

2. Add your Anthropic API key to `.env`:
ANTHROPIC_API_KEY=your_key_here

3. Install dependencies:
```bash
uv sync
```

4. Run:
```bash
uv run python main.py
```

## Result

The agent identified **Jeremy Bowers** as the murderer, hired by **Miranda Priestly** — following clues across crime scene reports, witness interviews, gym membership records and car plate matches.

