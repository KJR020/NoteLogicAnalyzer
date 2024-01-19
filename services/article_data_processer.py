import requests
import pandas as pd
import json


CONTENTS_API_URL = "https://note.com/api/v3/notes"


def fetch_trend_articles(api_url: str) -> pd.DataFrame:
    """noteAPIからトレンド記事データを取得し、DataFrameとして返す

    Args:
        API_URL (str): APIのURL

    Returns:
        pd.DataFrame: APIから取得したトレンド記事データ
    """
    res = requests.get(api_url)
    df_response = pd.read_json(res.text)
    return pd.DataFrame(df_response["data"].to_dict()).T
