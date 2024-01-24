import pytest

from src.services.article_data_processor import NoteApiDataFetcher


class TestNoteApiDaFetcher:
    def test_動作チェック(self):
        assert True

    def test_APIから記事データを取得できる(self):
        note_api_data_fetcher = NoteApiDataFetcher(
            api_url="https://note.com/api/v3/notes"
        )
        df = note_api_data_fetcher.fetch_data()
        assert df is not None, "DataFrame is None"
        assert not df.empty, "DataFrame is empty"
