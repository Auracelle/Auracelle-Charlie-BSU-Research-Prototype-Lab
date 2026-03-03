import streamlit as st
from src.config import DEFAULT_ACTORS, DEFAULT_POLICIES

def default_actors():
    return DEFAULT_ACTORS

def default_policies():
    return DEFAULT_POLICIES

def run_simulation_round(round_id: int, inject: str, actor: str, action: str, rationale: str, confidence: int):
    # Minimal turn record (extend with metrics, network effects, MARL hooks, etc.)
    record = {
        "round": round_id,
        "inject": inject,
        "actor": actor,
        "action": action,
        "confidence": confidence,
        "rationale": rationale.strip(),
    }
    st.session_state["turn_log"].append(record)

    # Placeholder outcome model
    outcome = {
        "status": "ok",
        "recorded": record,
        "notes": "Outcome engine is stubbed. Port your scoring/MARL logic from the notebook into src/ as you iterate.",
    }
    return outcome
