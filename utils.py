import csv
from models.Movie import Movie
from models.Link import Link
from models.Tag import Tag
from models.Rating import Rating


def read_movies():
    movies = []
    with open('data/movies.csv', 'r', encoding="utf8") as f:
        csvka = csv.reader(f, delimiter=',')
        header = next(csvka)  # Skip pierwszej linii
        for i, row in enumerate(csvka):
            movies.append(Movie(movieId=row[0],
                                title=row[1],
                                genres=row[2]
                                ).__dict__()
                          )
    return movies


def read_links():
    links = []
    with open('data/links.csv', 'r', encoding="utf8") as f:
        csvka = csv.reader(f, delimiter=',')
        header = next(csvka)  # Skip pierwszej linii
        for i, row in enumerate(csvka):
            links.append(Link(movieId=row[0],
                              imdbId=row[1],
                              tmdbId=row[2]
                              ).__dict__()
                         )
    return links


def read_tags():
    tags = []
    with open('data/tags.csv', 'r', encoding="utf8") as f:
        csvka = csv.reader(f, delimiter=',')
        header = next(csvka)  # Skip pierwszej linii
        for i, row in enumerate(csvka):
            tags.append(Tag(userId=row[0],
                            movieId=row[1],
                            tag=row[2],
                            timestamp=row[3]).__dict__()
                        )
    return tags


def read_ratings():
    ratings = []
    with open('data/ratings.csv', 'r', encoding="utf8") as f:
        csvka = csv.reader(f, delimiter=',')
        header = next(csvka)  # Skip pierwszej linii
        for i, row in enumerate(csvka):
            ratings.append(Rating(userId=row[0],
                                  movieId=row[1],
                                  rating=row[2],
                                  timestamp=row[3]).__dict__()
                           )
    return ratings
