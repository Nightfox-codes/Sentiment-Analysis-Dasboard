import os
import pandas as pd
from config import *
from cleaner import clean_text
from transformer import *
from validator import validate
from exporter import save

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE_DIR, "input", "Customer Feedback.csv")
OUTPUT = os.path.join(BASE_DIR, "output", "clean_customer_feedback.csv")

df=pd.read_csv(INPUT)
df.rename(columns=HEADER_MAP,inplace=True)
validate(df)

for c in df.select_dtypes(include=["object", "string"]).columns:
    df[c]=df[c].apply(clean_text)

if "Partner Name" in df.columns:
    df["Partner Name"]=df["Partner Name"].apply(standardize_partner)

if "Called Date" in df.columns:
    df["Called Date"]=df["Called Date"].apply(convert_called_date)

for c in df.columns:
    name_lower = c.lower()
    if "expectations" in name_lower:
        df[c] = case_insensitive_replace(df[c], EXPECTATION_MAP)
    elif "proactive" in name_lower:
        df[c] = case_insensitive_replace(df[c], PROACTIVE_MAP)
    elif "skill" in name_lower:
        df[c] = case_insensitive_replace(df[c], SKILL_MAP)
    elif any(kw in name_lower for kw in ("did ", "has ", "trouble", "arrange a call")):
        df[c] = case_insensitive_replace(df[c], YES_NO_MAP)

save(df,OUTPUT)
print("Done")
