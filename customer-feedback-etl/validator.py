import pandas as pd
REQUIRED=["Partner Name","Organization","Called Date"]
def validate(df):
    missing=[c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df
