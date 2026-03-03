import streamlit as st
from src.state import init_session_state, reset_session
from src.ui import section_title

st.set_page_config(page_title="Admin", page_icon="🧰", layout="wide")

init_session_state()
section_title("Admin", "Session controls + debug")

st.markdown("#### Session state")
st.json({k: v for k, v in st.session_state.items() if k not in ("_secrets",)})

st.markdown("---")
if st.button("Reset session state", type="primary"):
    reset_session()
    st.success("Session state reset. Refresh the page.")
