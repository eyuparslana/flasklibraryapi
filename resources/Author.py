from flask import request
from flask_restful import Resource
from models import db, Author, AuthorSchema

authors_schema = AuthorSchema(many=True)
author_schema = AuthorSchema()


class AuthorResource(Resource):
    def get(self, author_id):
        '''GET method to list an author'''

        pass

    def put(self, author_id):
        '''PUT method to update an author'''

        pass

    def delete(self, author_id):
        '''DELETE method to delete an author'''

        pass


class AuthorListResource(Resource):

    def get(self):
        '''GET method to list all authors'''

        pass

    def post(self):
        '''POST method to create an author'''

        pass
