# Porting Guide (Notebook → Streamlit modules)

Recommended port order:

1) **State + logging**
- Ensure turns/injects are captured reliably (already stubbed).

2) **Simulation mechanics**
- Move scoring functions and any RL/MARL stubs into `src/simulation.py`.

3) **Influence + maps**
- Keep graphs in `src/influence.py`.
- Add `src/maps.py` if you bring in geopolitics mapping.

4) **Real-world data**
- Add a `src/worldbank.py` / `src/sipri.py` etc and call from `src/data_providers.py`.

As you port, keep functions pure where possible (inputs → outputs) and keep Streamlit UI code in pages.
