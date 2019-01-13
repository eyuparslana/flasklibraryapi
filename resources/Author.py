from flask import request
from flask_restful import Resource
from models import db, Author, AuthorSchema

authors_schema = AuthorSchema(many=True)
author_schema = AuthorSchema()


class AuthorResource(Resource):
    def get(self, author_id):
        """GET method to list an author"""

        author = Author.query.get(author_id)
        author = author_schema.dump(author).data
        return {'status': 'success', 'data': author}, 200


    def put(self, author_id):
        """PUT method to update an author"""

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = author_schema.load(json_data)
        if errors:
            return errors, 422

        author = Author.query.filter_by(id=author_id).first()
        if not author:
            return {'message': 'Genre does not exist'}, 400

        author.first_name = data.first_name
        author.last_name = data.last_name

        db.session.commit()

        result = author_schema.dump(author).data
        return {'status': 'success', 'data': result}, 200

    def delete(self, author_id):
        """DELETE method to delete an author"""

        author = Author.query.get(author_id)
        if not author:
            return {'message': 'No Author Data'}, 400
        db.session.delete(author)
        db.session.commit()

        result = author_schema.dump(author).data
        return {"status": 'success', 'data': result}, 200


class AuthorListResource(Resource):
    def get(self):
        """GET method to list all authors"""

        authors = Author.query.filter_by().order_by(Author.id)
        authors = authors_schema.dump(authors).data
        return {'status': 'success', 'data': authors}, 200

    def post(self):
        """POST method to create an author"""

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400

        data, errors = author_schema.load(json_data)
        if errors:
            return errors, 422

        author = Author.query.filter_by(
            first_name=data.first_name, last_name=data.last_name).first()

        if author:
            return {'message': 'Author already exists'}, 400

        author = Author(
            first_name=data.first_name,
            last_name=data.last_name
        )

        db.session.add(author)
        db.session.commit()

        result = author_schema.dump(author).data
        return {'status': 'success', 'data': result}, 201


class AuthorSearch(Resource):
    def get(self):
        return {'message': 'Must be POST'}, 400

    def post(self):
        """POST method to create an author"""
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input provided'}, 400

        data, errors = author_schema.load(json_data)
        raw_result = Author.query.filter_by(**data)

        result = authors_schema.dump(raw_result).data

        if len(result) == 0:
            return {'message': 'No author provided'}, 200
            
        return result
