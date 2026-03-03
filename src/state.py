import streamlit as st

def init_session_state():
    # Core session keys
    st.session_state.setdefault("round_id", 1)
    st.session_state.setdefault("inject", "")
    st.session_state.setdefault("turn_log", [])
    st.session_state.setdefault("inject_log", [])
    st.session_state.setdefault("confidence", 65)

def reset_session():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
