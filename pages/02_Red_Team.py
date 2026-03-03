import streamlit as st
from src.state import init_session_state
from src.ui import section_title
from src.red_team import default_injects, apply_inject

st.set_page_config(page_title="Red Team", page_icon="🧨", layout="wide")

init_session_state()
section_title("Red Team Module", "Adversarial injects + stress‑test probes")

st.markdown(
    """
Use this page to apply structured injects that challenge assumptions, coordination, and institutional capacity.
Each inject should be tied to **observable effects** and **evidence prompts**.
"""
)

inject = st.selectbox("Select an inject", options=default_injects(), key="rt_inject")
notes = st.text_area("Facilitator notes", height=120, key="rt_notes")

if st.button("Apply inject", type="primary"):
    result = apply_inject(inject=inject, notes=notes)
    st.success("Inject applied to session state.")
    st.json(result)

st.markdown("---")
st.subheader("Inject history")
st.dataframe(st.session_state.get("inject_log", []), use_container_width=True)
