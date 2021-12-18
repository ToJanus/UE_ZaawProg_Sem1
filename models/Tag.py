class Tag:
    def __init__(self, userId, movieId, tag, timestamp) -> None:
        self._userId = int(userId) if userId != '' else None
        self._movieId = int(movieId) if movieId != '' else None
        self._tag = tag
        self._timestamp = int(timestamp) if timestamp != '' else None

    @property
    def userId(self) -> int:
        return self._userId

    @userId.setter
    def userId(self, value: int) -> None:
        self._userId = value

    @property
    def movieId(self) -> int:
        return self._movieId

    @movieId.setter
    def movieId(self, value: int) -> None:
        self._movieId = value

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, value: str) -> None:
        self._tag = value

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int) -> None:
        self._timestamp = value

    def __dict__(self) -> dict:
        return {'userId': self._userId,
                'movieId': self._movieId,
                'tag': self._tag,
                'timestamp': self._timestamp
                }
