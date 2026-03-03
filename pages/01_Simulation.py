import streamlit as st
from src.state import init_session_state
from src.ui import section_title, render_policy_assess_popover
from src.simulation import run_simulation_round, default_actors, default_policies

st.set_page_config(page_title="Simulation", page_icon="🎛️", layout="wide")

init_session_state()
section_title("Simulation", "Rounds / injects / actor turns + evidence capture")

colA, colB = st.columns([2, 1], vertical_alignment="top")

with colA:
    st.markdown("#### Scenario controls")
    round_id = st.number_input("Round", min_value=1, value=int(st.session_state.get("round_id", 1)), step=1)
    inject = st.text_input("Inject (optional)", value=st.session_state.get("inject", ""))
    st.session_state["round_id"] = int(round_id)
    st.session_state["inject"] = inject

    st.markdown("#### Actor turn")
    actor = st.selectbox("Actor", options=default_actors(), key="actor")
    action = st.selectbox("Governance action", options=default_policies(), key="policy_move")

    render_policy_assess_popover(actor=actor, policy=action)

    rationale = st.text_area("Decision rationale (evidence + assumptions)", key="rationale", height=140)
    confidence = st.slider("Evidentiary confidence", 0, 100, int(st.session_state.get("confidence", 65)), 1)
    st.session_state["confidence"] = int(confidence)

    if st.button("Commit turn", type="primary", use_container_width=True):
        outcome = run_simulation_round(
            round_id=int(round_id),
            inject=inject,
            actor=actor,
            action=action,
            rationale=rationale,
            confidence=int(confidence),
        )
        st.success("Turn recorded.")
        st.json(outcome)

with colB:
    st.markdown("#### Session log")
    log = st.session_state.get("turn_log", [])
    st.caption(f"Turns recorded: {len(log)}")
    if log:
        st.dataframe(log, use_container_width=True, height=420)

    st.markdown("#### Export")
    if st.button("Export session JSON", use_container_width=True):
        from src.export import export_json
        payload = export_json()
        st.download_button(
            "Download session.json",
            data=payload,
            file_name="auracelle_charlie_session.json",
            mime="application/json",
            use_container_width=True,
        )
