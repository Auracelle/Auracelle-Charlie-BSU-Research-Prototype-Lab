    import streamlit as st
    from src.config import APP_TITLE, APP_CAPTION

    def render_header():
        st.title(APP_TITLE)
        st.caption(APP_CAPTION)

    def section_title(title: str, subtitle: str = ""):
        st.title(title)
        if subtitle:
            st.caption(subtitle)

    def render_quick_links():
        with st.expander("📌 Quick links / demo access", expanded=False):
            st.markdown("- GitHub Pages prototype (if applicable): add your link here")
            st.markdown("- Live sandbox (if applicable): add your link here")

    def render_run_notes():
        with st.expander("📘 Run notes", expanded=False):
            st.markdown(
                """
    - This repo is structured for **Streamlit Cloud** (Path A).
    - Each page uses a shared session state (`st.session_state`) for turns and injects.
    - Replace demo providers with your real modules as you port logic from the notebook.
                """
            )

    def render_policy_assess_popover(actor: str, policy: str):
        with st.popover("🔎 Assess a Policy"):
            st.markdown(
                f"""**Actor:** {actor}

**Policy:** {policy}

Use this prompt to record:
- Acceptance likelihood (0–100)
- Key incentives / objections
- Second‑order effects
- What might break if adopted
"""
            )
