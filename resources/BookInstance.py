from flask import request
from flask_restful import Resource
from models import db, Book, BookInstance, BookInstanceSchema


book_instances_schema = BookInstanceSchema(many=True)
book_instance_schema = BookInstanceSchema()


class BookInstanceResource(Resource):
    def get(self, book_instance_id):
        '''GET method to list a book instance'''

        book_instance = BookInstance.query.get(book_instance_id)
        book_instance = book_instance_schema.load(book_instance).data
        return {'status': 'success', 'data': book_instance}, 200

    def put(self, book_instance_id):
        '''PUT method to update a book instance'''

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = book_instance_schema.load(json_data)
        if errors:
            return errors, 422

        # Get book instance
        book_instance = BookInstance.query.filter_by(
            id=book_instance_id).first()
        if not book_instance:
            return {'message': 'Book instance does not exist'}, 400

        # Update book instance
        book_instance.status = data['status'],
        book_instance.due_back = data.get('due_back', None),

        db.session.commit()

        result = book_instance_schema.dump(book_instance).data
        return {"status": 'success', 'data': result}, 204

    def delete(self, book_instance_id):
        '''DELETE method to delete a book instance'''

        book_instance = BookInstance.query.filter_by(
            id=book_instance_id).delete()

        db.session.commit()

        result = book_instance_schema.dump(book_instance).data
        return {"status": 'success', 'data': result}, 204


class BookInstanceListResource(Resource):

    def get(self):
        '''GET method to list all book instances'''

        book_instances = BookInstance.query.all()
        book_instances = book_instances_schema.load(book_instances).data
        return {'status': 'success', 'data': book_instances}, 200

    def post(self):
        '''POST method to create a book instance'''

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input provided'}, 400

        data, errors = book_instance_schema.load(json_data)
        if errors:
            return errors, 422

        # Book control
        book = Book.query.filter_by(id=data['book_id']).first()
        if not book:
            return {'status': 'error', 'message': 'book not found'}, 400

        book_instance = BookInstance(
            status=data['status'],
            due_back=data.get('due_back', None),
            book_id=data['book_id']
        )

        db.session.add(book_instance)
        db.session.commit()

        result = book_instance_schema.dump(book_instance).data
        return {'status': 'success', 'data': result}, 201
