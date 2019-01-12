from flask import request
from flask_restful import Resource
from models import db, Genre, GenreSchema

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreResource(Resource):
    def get(self, genre_id):
        '''GET method to list a genre'''

        pass

    def put(self, genre_id):
        '''PUT method to update a genre'''

        pass

    def delete(self, genre_id):
        '''DELETE method to delete a genre'''

        pass


class GenreListResource(Resource):
    def get(self):
        '''GET method to list all genres'''

        pass

    def post(self):
        '''POST method to create a genre'''

        pass
