class Movie:

    def __init__(self, movieId, title, genres) -> None:  # movieId,title,genres
        self._movieId = int(movieId) if movieId != '' else None
        self._title = title
        self._genres = genres

    @property
    def movieId(self) -> int:
        return self._movieId

    @movieId.setter
    def movieId(self, value: int) -> None:
        self._movieId = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def genres(self) -> str:
        return self._genres

    @genres.setter
    def genres(self, value: str) -> None:
        self._genres = value

    def __dict__(self) -> dict:
        return {'movieId': self._movieId,
                'title': self._title,
                'genres': self._genres}
