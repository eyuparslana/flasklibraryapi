from flask import jsonify, request, abort, make_response
from models import BookInstance
from schemas import BookInstanceSchema
from extensions import db

BASE_URL = '/libraryapp/api'


def create_routes(app):

    def make_path(resource):
        return "".join([BASE_URL, resource])

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({"error": "Bad request"}), 400)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({"error": "Not found"}), 404)

    @app.route('/')
    def index():
        return "Welcome"

    @app.route(BASE_URL)
    def api_index():
        return "This is the index of API endpoint"

    @app.route(make_path('/BookInstances'), methods=['POST'])
    def create_book_instance():
        if not request.json:
            abort(400)

        try:
            book_id = int(request.json['book_id'])
            status = str(request.json['status'])
            due_back = str(request.json['due_back'])

            book_instance = BookInstance(
                book_id=book_id,
                status=status,
                due_back=due_back
            )

            db.session.add(book_instance)
            db.session.commit()
            return jsonify({"result": "success"}), 201
        except KeyError:
            abort(400)
        except Exception:
            db.session.rollback()
            abort(404)

    @app.route(make_path('/BookInstances'), methods=['GET'])
    def get_all_book_instances():
        try:
            book_instances = BookInstance.query.all()
            output = [BookInstanceSchema().dump(
                instance).data for instance in book_instances]
            return jsonify({'book_instances': output}), 200
        except Exception:
            abort(404)

    @app.route(make_path('/BookInstances/<int:id>'), methods=['GET'])
    def get_book_instance(id):
        try:
            book_instance = BookInstance.query.get(id)
            output = BookInstanceSchema().dump(book_instance).data
            return jsonify({'book_instance': output}), 200
        except Exception:
            abort(404)

    @app.route(make_path('/BookInstances/<int:id>'), methods=['PATCH'])
    def update_book_instance(id):
        if not request.json:
            abort(404)

        try:
            book_id = int(request.json['book_id'])
            status = str(request.json['status'])
            due_back = str(request.json['due_back'])

            book_instance = BookInstance.query.get(id)

            book_instance.book_id = book_id
            book_instance.status = status
            book_instance.due_back = due_back

            db.session.commit()
            return jsonify({"result": "success"}), 200
        except KeyError:
            abort(400)
        except Exception:
            db.session.rollback()
            abort(404)

    @app.route(make_path('/BookInstances/<int:id>'), methods=['DELETE'])
    def delete_book_instance(id):
        try:
            book_instance = BookInstance.query.get(id)
            db.session.delete(book_instance)
            db.session.commit()

            return jsonify({"result": "success"}), 200
        except Exception:
            db.session.rollback()
            abort(404)
