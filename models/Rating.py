class Rating:
    def __init__(self, userId, movieId, rating, timestamp) -> None:
        self._userId = int(userId) if userId != '' else None
        self._movieId = int(movieId) if movieId != '' else None
        self._rating = float(rating) if rating != '' else None
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
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, value: float) -> None:
        self._rating = value

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int) -> None:
        self._timestamp = value

    def __dict__(self) -> dict:
        return {'userId': self._userId,
                'movieId': self._movieId,
                'rating': self._rating,
                'timestamp': self._timestamp
                }
