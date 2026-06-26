import pandas as pd
from config import VALID_PARTNERS, PARTNER_MAP

def standardize_partner(v):
    if pd.isna(v): return v
    key = str(v).strip().lower()
    mapped = PARTNER_MAP.get(key, str(v).strip())
    if mapped not in VALID_PARTNERS:
        raise ValueError(f"Unknown partner: {v}")
    return mapped

def convert_called_date(v):
    if pd.isna(v): return None
    s=str(v).strip().replace("-","/")
    s=s.split()[0]
    for f in ("%d/%m/%Y", "%d/%m/%y", "%m/%d/%Y", "%m/%d/%y", "%Y/%m/%d", "%Y-%m-%d"):
        try:
            return pd.to_datetime(s,format=f).strftime("%Y-%m-%d")
        except: pass
    raise ValueError(f"Bad date: {v}")

def case_insensitive_replace(series, mapping_dict):
    lower_map = {str(k).strip().lower(): v for k, v in mapping_dict.items()}
    return series.apply(lambda val: lower_map.get(str(val).strip().lower(), val) if not pd.isna(val) else val)
