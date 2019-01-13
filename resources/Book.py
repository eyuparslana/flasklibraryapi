from flask import request
from flask_restful import Resource
from models import db, Author, Book, BookSchema

books_schema = BookSchema(many=True)
book_schema = BookSchema()


class BookResource(Resource):
    def get(self, book_id):
        """
        GET method to list a book
        """

        book = Book.query.get(book_id)
        book = book_schema.dump(book).data
        return {'status': 'success', 'data': book}, 200

    def put(self, book_id):
        """
        PUT method to update a book
        """

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = book_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.rollback()

        # Get book
        book = Book.query.filter_by(id=book_id).first()
        if not book:
            return {'message': 'Book does not exist'}, 400

        # Author control
        author = Author.query.filter_by(id=data.author_id).first()
        if not author:
            return {'status': 'error', 'message': 'book author not found'}, 400

        # Genres control
        for genre in data.genres:
            if not genre.name:
                return {'status': 'error', 'message': 'genre not found'}, 400

        # Update book
        book.title = data.title
        book.isbn = data.isbn
        book.publish_date = data.publish_date
        book.author_id = data.author_id
        book.author = author
        book.genres = data.genres

        db.session.commit()

        result = book_schema.dump(book).data
        return {"status": 'success', 'data': result}, 200

    def delete(self, book_id):
        """
        DELETE method to delete a book
        """

        book = Book.query.filter_by(id=book_id).delete()

        db.session.commit()

        result = book_schema.dump(book).data
        return {"status": 'success', 'data': result}, 200


class BookListResource(Resource):
    def get(self):
        """
        GET method to list all books
        """

        books = Book.query.filter_by().order_by(Book.id)
        books = books_schema.dump(books).data
        return {'status': 'success', 'data': books}, 200

    def post(self):
        """
        POST method to create a book
        """

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400

        data, errors = book_schema.load(json_data)
        if errors:
            return errors, 422
        db.session.rollback()
        book = Book.query.filter_by(title=data.title).first()
        if book:
            return {'message': 'Book already exists'}, 400

        # Author control
        author = Author.query.filter_by(id=data.author_id).first()
        if not author:
            return {'status': 'error', 'message': 'book author not found'}, 400

        # Genres control
        for genre in data.genres:
            if not genre.name:
                return {'status': 'error', 'message': 'genre not found'}, 400
        book = data

        db.session.add(book)
        db.session.commit()

        result = book_schema.dump(book).data
        return {'status': 'success', 'data': result}, 201
