import pytest

from services.article_data_processer import fetch_trend_articles


class TestArticleDataProcesser:
    def test_動作チェック(self):
        assert False

    def test_動作チェック2(self):
        assert True

    def test_apiから記事データを取得できる(self):
        df = fetch_trend_articles("https://note.com/api/v3/notes")
        assert df is not None
