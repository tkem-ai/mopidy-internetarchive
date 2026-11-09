import logging

from mopidy import backend

from . import translator

logger = logging.getLogger(__name__)


class InternetArchivePlaybackProvider(backend.PlaybackProvider):
    def translate_uri(self, uri):
        identifier, filename, _ = translator.parse_uri(uri)
        if identifier and filename:
            return self.backend.client.geturl(identifier, filename)
        logger.error("Cannot play %s: not a track URI", uri)
        return None
