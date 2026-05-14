import pytest
from unittest.mock import MagicMock, patch
from rick_morty_client import RickMortyClient

def test_get_characters_success():
    client = RickMortyClient()
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": [{"name": "Rick Sanchez"}]}
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        res = client.get_characters()
        assert res["results"][0]["name"] == "Rick Sanchez"






