from flask import request
from flask_restful import Resource
from models import db, Genre, Author, Book, BookSchema

books_schema = BookSchema(many=True)
book_schema = BookSchema()


class BookResource(Resource):
    def get(self, book_id):
        '''GET method to list a book'''

        pass

    def put(self, book_id):
        '''PUT method to update a book'''

        pass

    def delete(self, book_id):
        '''DELETE method to delete a book'''

        pass


class BookListResource(Resource):
    def get(self):
        '''GET method to list all books'''

        pass

    def post(self):
        '''POST method to create a book'''

        pass
