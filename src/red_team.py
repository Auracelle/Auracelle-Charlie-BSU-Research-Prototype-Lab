import streamlit as st
import datetime

def default_injects():
    return [
        "Adversarial misinformation surge",
        "Supply-chain compromise cascade",
        "Regulatory fragmentation across allies",
        "Attribution uncertainty / false flag",
        "Critical infrastructure safety incident",
    ]

def apply_inject(inject: str, notes: str = ""):
    entry = {
        "ts": datetime.datetime.utcnow().isoformat() + "Z",
        "inject": inject,
        "notes": notes.strip(),
    }
    st.session_state["inject_log"].append(entry)
    # Mirror into current inject field for Simulation page convenience
    st.session_state["inject"] = inject
    return {"applied": True, "entry": entry}
