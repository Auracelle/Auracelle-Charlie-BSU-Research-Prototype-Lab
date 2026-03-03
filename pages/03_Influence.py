import streamlit as st
from src.state import init_session_state
from src.ui import section_title
from src.influence import demo_network, compute_pagerank

st.set_page_config(page_title="Influence", page_icon="🕸️", layout="wide")

init_session_state()
section_title("Influence Network", "Network view + PageRank-style influence scoring")

G = demo_network()
pr = compute_pagerank(G)

st.markdown("#### Influence ranking (PageRank)")
st.dataframe(pr, use_container_width=True, height=420)

st.markdown("---")
st.caption("Tip: connect this to your real actor graph + weights once your data providers are wired.")
