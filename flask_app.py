from flask import Flask
from flask_restful import Resource, Api

from utils import read_movies, read_tags, read_links, read_ratings

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world', 'dwa': ['raz', 'piec']}


class Movies(Resource):
    def get(self):
        return read_movies()


class Links(Resource):
    def get(self):
        return read_links()


class Tags(Resource):
    def get(self):
        return read_tags()


class Ratings(Resource):
    def get(self):
        return read_ratings()


api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Tags, '/tags')
api.add_resource(Ratings, '/ratings')
