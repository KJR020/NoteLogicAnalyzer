# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

from services.article_data_processor import NoteApiDataFetcher

LOGGER = get_logger(__name__)

ARTICLE_DATA_PROCESSOR = NoteApiDataFetcher()


def initial_fetch_articles():
    return df


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    df_trend_articles = ARTICLE_DATA_PROCESSOR.fetch_data()

    st.write("# デモアプリです")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Noteのトレンド記事をAPIから取得し、
        分析してみました.
        """
    )

    st.table(df_trend_articles.loc[:, ["name", "publish_at", "user", "like_count"]])


if __name__ == "__main__":
    run()
