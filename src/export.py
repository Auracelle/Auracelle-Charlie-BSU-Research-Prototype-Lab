import json
import streamlit as st

def export_json():
    payload = {
        "round_id": st.session_state.get("round_id"),
        "turn_log": st.session_state.get("turn_log", []),
        "inject_log": st.session_state.get("inject_log", []),
    }
    return json.dumps(payload, indent=2)
