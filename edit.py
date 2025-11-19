
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent
ENV_FILE = ROOT_DIR / "OPENAI_API_KEY.txt"
DATA_FILE = ROOT_DIR / "data.csv"


def load_api_key(env_path: Path = ENV_FILE) -> str:
	"""Load OPENAI_API_KEY from the environment or CHAT_GPTAPI.txt."""

	existing = os.getenv("OPENAI_API_KEY")
	if existing:
		return existing

	if not env_path.exists():
		raise FileNotFoundError(f"Environment file not found: {env_path}")

	with env_path.open(encoding="utf-8") as handle:
		for raw_line in handle:
			line = raw_line.strip()
			if not line or line.startswith("#"):
				continue
			if "=" not in line:
				continue
			key, value = line.split("=", 1)
			if key.strip() == "OPENAI_API_KEY":
				cleaned = value.strip().strip('"').strip("'")
				if not cleaned:
					break
				os.environ["OPENAI_API_KEY"] = cleaned
				return cleaned

	raise RuntimeError(f"OPENAI_API_KEY was not found in {env_path}")


def build_openai_client():
	"""Create an OpenAI client after ensuring the SDK is available."""

	try:
		from openai import OpenAI
	except ImportError as exc:  # pragma: no cover - dependency guard
		raise SystemExit(
			"Missing dependency 'openai'. Install it with `pip install openai`."
		) from exc

	api_key = load_api_key()
	return OpenAI(api_key=api_key)


client = build_openai_client()

df = pd.read_csv(DATA_FILE)
df_row = 222
df_title = df.loc[df_row]['title']
df_price = df.loc[df_row]['closed_price']

prompt = f"Search the follow title with closed price: {df_title}, {df_price} and normalize the title to BRAND NAME and MODEL ID."

response = client.responses.create(
		model="gpt-5",
		input=prompt
	)

print(response.output_text)


