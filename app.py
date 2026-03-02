import streamlit as st
from pathlib import Path
import json

st.set_page_config(
    page_title="Auracelle Charlie — BSU Prototype",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Auracelle Charlie — BSU Prototype")
st.caption("Streamlit entrypoint for the Bath Spa prototype repository (notebook-first build).")

st.markdown(
    """
**What this app is**
- A lightweight **launcher + run guide** for the repository.
- It provides a consistent entrypoint for local runs or Streamlit Cloud deployments.

**Primary research artifact**
- The canonical implementation remains the notebook: `Auracelle_Charlie_BSU_Prototype_2026-02-26.ipynb`
"""
)

repo_root = Path(__file__).resolve().parent
nb_path = repo_root / "Auracelle_Charlie_BSU_Prototype_2026-02-26.ipynb"

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
    st.subheader("Run options")
    st.markdown(
        """
**Option A — Google Colab**
1. Push this repo to GitHub.
2. Open the notebook in Colab (File → Open notebook → GitHub).
3. Run cells top-to-bottom.

**Option B — Local**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
        """
    )

    if nb_path.exists():
        with open(nb_path, "rb") as f:
            st.download_button(
                "⬇️ Download the notebook (.ipynb)",
                data=f,
                file_name=nb_path.name,
                mime="application/x-ipynb+json",
                use_container_width=True,
            )
    else:
        st.warning("Notebook not found in repo root. Ensure it is committed alongside app.py.")

with col2:
    st.subheader("Repository health check")
    checks = {
        "Notebook present": nb_path.exists(),
        "requirements.txt present": (repo_root / "requirements.txt").exists(),
        "docs/ETHICS.md present": (repo_root / "docs" / "ETHICS.md").exists(),
        "docs/RUNBOOK.md present": (repo_root / "docs" / "RUNBOOK.md").exists(),
    }
    for k, v in checks.items():
        st.write(f"{'✅' if v else '⚠️'} {k}")

    st.markdown("---")
    st.subheader("Optional: notebook metadata")
    if nb_path.exists():
        try:
            nb_json = json.loads(nb_path.read_text(encoding="utf-8"))
            st.write(
                {
                    "kernelspec": nb_json.get("metadata", {}).get("kernelspec", {}),
                    "language_info": nb_json.get("metadata", {}).get("language_info", {}),
                    "cell_count": len(nb_json.get("cells", [])),
                }
            )
        except Exception as e:
            st.error(f"Could not parse notebook JSON: {e}")

st.markdown("---")
st.subheader("Next step (recommended)")
st.markdown(
    """
If you want this repo to run as a **full multi-page Streamlit app** (not just a launcher),
the next engineering step is to refactor the notebook into:
- `app.py` (navigation + shared state)
- `pages/` modules (Simulation, Red Team, Influence, Real-World Data, etc.)
- a small `/src` package for shared utilities

This keeps the research instrument reproducible and deployable.
"""
)
