import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DATA_FILE = ROOT_DIR / "data.csv"

df = pd.read_csv(DATA_FILE)

title_list = df.loc[:]['title']

title_list = title_list.str.strip()

print(title_list.head())

title_list.to_csv("title_dataset.csv")
