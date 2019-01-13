from flask import request
from flask_restful import Resource
from models import db, Genre, GenreSchema

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreResource(Resource):
    def get(self, genre_id):
        """GET method to list a genres"""

        genre = Genre.query.get(genre_id)
        genre = genre_schema.dump(genre).data
        return {'status': 'success', 'data': genre}, 200

    def put(self, genre_id):
        """PUT method to update a genre"""

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = genre_schema.load(json_data)
        if errors:
            return errors, 422

        genre = Genre.query.filter_by(id=genre_id).first()
        if not genre:
            return {'message': 'Genre does not exist'}, 400

        genre.name = data.name
        db.session.commit()

        result = genre_schema.dump(genre).data
        return {"status": 'success', 'data': result}, 200

    def delete(self, genre_id):
        """DELETE method to delete a genre"""

        genre = Genre.query.get(genre_id)
        if not genre:
            return {'message': 'No Genre Data'}, 400
        db.session.delete(genre)
        db.session.commit()

        result = genre_schema.dump(genre).data
        return {"status": 'success', 'data': result}, 200


class GenreListResource(Resource):
    def get(self):
        """GET method to list all genres"""

        genres = Genre.query.filter_by().order_by(Genre.id)
        genres = genres_schema.dump(genres).data
        return {'status': 'success', 'data': genres}, 200

    def post(self):
        """POST method to create a genre"""

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = genre_schema.load(json_data)
        if errors:
            return errors, 422

        genre = Genre.query.filter_by(name=data.name).first()
        if genre:
            return {'message': 'Genre already exists'}, 400

        genre = Genre(name=json_data.name)

        db.session.add(genre)
        db.session.commit()

        result = genre_schema.dump(genre).data
        return {"status": 'success', 'data': result}, 201
