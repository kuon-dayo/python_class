import pandas as pd
import os
import urllib.request
import re
import csv
import tarfile
import safetensors
import unidic_lite
from transformers import AutoTokenizer, AutoModelForMaskedLM, BertJapaneseTokenizer

tokenizer = AutoTokenizer.from_pretrained("tohoku-nlp/bert-base-japanese-whole-word-masking")
model = AutoModelForMaskedLM.from_pretrained("tohoku-nlp/bert-base-japanese-whole-word-masking")


# データの読み込み
df = pd.read_csv("title_dataset.csv", index_col=0 )

titles = df.title.values
# データの確認
print(titles[:5])  # 最初の5件を表示

## テスト実行
# 元文章
print(' Original: ', titles[0])
# Tokenizer
print('Tokenized: ', tokenizer.tokenize(titles[0]))
# Token-id
print('Token IDs: ', tokenizer.convert_tokens_to_ids(tokenizer.tokenize(titles[0])))