class Link:
    def __init__(self, movieId, imdbId, tmdbId) -> None:
        self._movieId = int(movieId) if movieId != '' else None
        self._imdbId = int(imdbId) if imdbId != '' else None
        self._tmdbId = int(tmdbId) if tmdbId != '' else None

    @property
    def movieId(self) -> int:
        return self._movieId

    @movieId.setter
    def movieId(self, value: int) -> None:
        self._movieId = value

    @property
    def imdbId(self) -> int:
        return self._imdbId

    @imdbId.setter
    def imdbId(self, value: int) -> None:
        self._imdbId = value

    @property
    def tmdbId(self) -> int:
        return self._tmdbId

    @tmdbId.setter
    def tmdbId(self, value: int) -> None:
        if value != '':
            self._tmdbId = value
        else:
            self._tmdbId = None

    def __dict__(self) -> dict:
        return {'movieId': self._movieId,
                'imdbId': self._imdbId,
                'tmdbId': self._tmdbId
                }
