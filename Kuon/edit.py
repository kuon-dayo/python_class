import pandas as pd

df = pd.read_csv("yauc_dtm_closed.csv", header=None)

header = [
    "item_id",
    "item_url",
    "platform",
    "title",
    "category_lvl1",
    "category_lvl2",
    "category_lvl3",
    "closed_price",
    "start_price",
    "bids",
    "end_time_text",
    "free_shipping",
    "unused_flag",
    "image_url",
    "seller_url",
    "seller_id",
    "seller_rating_pct",
    "ship_from",
    "updated_at",
]

df.columns = header
df.to_csv("data.csv", index=False)

