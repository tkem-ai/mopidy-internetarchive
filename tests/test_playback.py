import pytest


def test_translate_url(playback, client_mock):
    url = "http://archive.org/download/item/file.mp3"
    client_mock.geturl.return_value = url
    result = playback.translate_uri("internetarchive:item#file.mp3")
    client_mock.geturl.assert_called_once()
    assert client_mock.geturl.call_args == (("item", "file.mp3"),)
    assert result == url


@pytest.mark.parametrize(
    "uri",
    [
        "internetarchive:",
        "internetarchive:item",
        "internetarchive:audio?sort=downloads+desc",
    ],
)
def test_translate_non_track_uri(playback, client_mock, uri):
    assert playback.translate_uri(uri) is None
    client_mock.geturl.assert_not_called()
