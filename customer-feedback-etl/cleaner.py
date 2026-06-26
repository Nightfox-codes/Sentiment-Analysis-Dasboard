import pandas as pd
def clean_text(v):
    if pd.isna(v): return v
    return " ".join(str(v).replace("\t"," ").replace("\n"," ").split()).strip()
