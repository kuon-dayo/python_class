import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
ENV_FILE = ROOT_DIR / "OPENAI_API_KEY.txt"
DATA_FILE = ROOT_DIR / "data.csv"

df = pd.read_csv(DATA_FILE)

df_row = 224
output_csv = df.loc[df_row]

output_csv.to_csv("output_row_224.csv",)
print(output_csv)