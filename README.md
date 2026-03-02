# Auracelle Charlie — Bath Spa Prototype (Notebook)

This repository contains the Bath Spa University prototype notebook for **Auracelle Charlie** (AGPO research instrument).

## Contents
- `Auracelle_Charlie_BSU_Prototype_2026-02-26.ipynb` — primary Jupyter/Colab notebook
- `requirements.txt` — minimal Python dependencies (adjust as needed)
- `environment.yml` — optional Conda environment definition
- `.github/workflows/` — CI helpers (notebook JSON validation)
- `docs/` — research, ethics, and runbook notes
- `CITATION.cff` — citation metadata for academic reuse

## Recommended ways to run
### 1) Google Colab (fastest)
1. Upload `Auracelle_Charlie_BSU_Prototype_2026-02-26.ipynb` to Colab (or open from GitHub after you push).
2. Run cells top-to-bottom.
3. If the notebook launches Streamlit, follow the printed local URL or your tunnel URL.

### 2) Local Jupyter
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Notes
- This is a research prototype used for **policy stress-testing** and wargaming evidence capture.
- Treat outputs as structured reflections and measurements — not predictions or operational guidance.

## License
See [LICENSE](LICENSE).

## Contact
PI: **Grace-Alice Evans**
