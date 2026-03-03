import streamlit as st
from src.state import init_session_state
from src.ui import section_title
from src.data_providers import fetch_demo_metrics

st.set_page_config(page_title="Real-World Data Metrics", page_icon="📊", layout="wide")

init_session_state()
section_title("Real-World Data Metrics", "Demo provider (wire to World Bank / SIPRI / ITU etc.)")

st.markdown(
    """
This page is a **starter**. Replace the demo provider with your production data modules.
"""
)

country = st.selectbox("Country / Actor", ["US", "UK", "China", "Japan", "Brazil", "India", "UAE", "NATO"])
metrics = fetch_demo_metrics(country)

st.json(metrics)
