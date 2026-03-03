# Auracelle Charlie — Bath Spa Prototype (Streamlit Cloud / Path A)

This repository is the **Path A** Streamlit Cloud structure for the Bath Spa Auracelle Charlie prototype.

## What changed vs notebook-only
- ✅ `app.py` is now a **real Streamlit app** (not a placeholder launcher).
- ✅ `pages/` provides multi‑page navigation (Simulation, Red Team, Influence, Real‑World Data, Admin).
- ✅ `src/` contains shared utilities (state, UI, stubs for engines/data).
- ✅ The original notebook is preserved under `notebooks/` for reference.

## Streamlit Cloud settings
- **Main file path:** `app.py`
- Python version: default is fine (3.11 is recommended)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Where to port your notebook logic
- Policy stress-test scoring + MARL stubs → `src/simulation.py`
- Inject library + evidence prompts → `src/red_team.py`
- Influence graph + geopolitics map → `src/influence.py` (and add `src/maps.py` later)
- API data providers → `src/data_providers.py`

## Repo layout
- `app.py`
- `pages/`
- `src/`
- `notebooks/` (original .ipynb)
- `docs/`

## License
MIT — see [LICENSE](LICENSE).

## Contact
PI: **Grace-Alice Evans**
