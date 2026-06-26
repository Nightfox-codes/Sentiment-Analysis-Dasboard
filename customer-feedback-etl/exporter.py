import os

def save(df,path):
    try:
        df.to_csv(path,index=False)
    except PermissionError:
        base, ext = os.path.splitext(path)
        alt_path = f"{base}_new{ext}"
        print(f"WARNING: Permission denied writing to {path}. Saving to {alt_path} instead.")
        df.to_csv(alt_path,index=False)
