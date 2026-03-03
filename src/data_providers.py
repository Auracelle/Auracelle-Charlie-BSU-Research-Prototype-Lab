import random

def fetch_demo_metrics(country: str):
    # Replace with World Bank / SIPRI / ITU modules as you port from notebook.
    return {
        "actor": country,
        "gdp_usd": int(random.uniform(0.5e12, 25e12)),
        "internet_penetration_pct": round(random.uniform(45, 99), 2),
        "mil_exp_usd": int(random.uniform(5e9, 900e9)),
        "notes": "Demo values (stub). Wire to real APIs in src/data_providers.py.",
    }
