import pandas as pd
import networkx as nx

def demo_network():
    G = nx.DiGraph()
    edges = [
        ("US", "UK", 0.6),
        ("US", "NATO", 0.7),
        ("China", "Brazil", 0.3),
        ("UK", "NATO", 0.5),
        ("Japan", "US", 0.4),
        ("India", "UAE", 0.2),
        ("NATO", "UK", 0.4),
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    return G

def compute_pagerank(G):
    pr = nx.pagerank(G, weight="weight")
    df = pd.DataFrame([{"node": k, "pagerank": v} for k, v in pr.items()]).sort_values("pagerank", ascending=False)
    return df
