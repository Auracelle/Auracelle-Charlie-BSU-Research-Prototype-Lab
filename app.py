import streamlit as st
from src.config import APP_TITLE, APP_CAPTION
from src.state import init_session_state
from src.ui import render_header, render_quick_links, render_run_notes

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()

render_header()

st.markdown(
    """
### Home
This is the **Streamlit Cloud entrypoint** for Auracelle Charlie (Bath Spa prototype).
Use the pages in the sidebar to run simulations, red team injects, influence analysis, and real‑world data views.

**Research stance:** transparent instrument for *stress‑testing* governance decisions — not a predictive oracle.
"""
)

render_quick_links()
render_run_notes()

st.markdown("---")
st.subheader("Notebook reference")
st.markdown(
    """
The original build remains preserved in:
- `notebooks/02_26_BATH_SPA_PROTOTYPE_READY_AURACELLE_CHARLIE_26_02_2026.ipynb`

This repository refactors the notebook into a reproducible, deployable Streamlit structure.
"""
)
