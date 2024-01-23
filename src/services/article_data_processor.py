#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import requests
import pandas as pd
import json


CONTENTS_API_URL = "https://note.com/api/v3/notes"


class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        pass


class NoteApiDataFetcher(DataFetcher):
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return pd.DataFrame(data["data"])
        except HTTPError as http_err:
            print(f"Error fetching data: {http_err}")
        except Exception as err:
            print(f"Error fetching data: {err}")

    def get_trend_articles(api_url: str) -> pd.DataFrame:
        """NoteAPIからトレンド記事データを取得し、DataFrameとして返す

        Args:
            API_URL (str): APIのURL

        Returns:
            pd.DataFrame: APIから取得したトレンド記事データ
        """
        res = requests.get(api_url)
        df_response = pd.read_json(res.text)
        return pd.DataFrame(df_response["data"].to_dict()).T
