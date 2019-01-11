from flask import jsonify, request, abort, make_response
from models import BookInstance, Book, Genre
from schemas import BookInstanceSchema, BookSchema, GenreSchema
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

    @app.route(make_path('/Books'), methods=['POST'])
    def create_book():
        if not request.json:
            abort(400)
        try:

            new_book = Book(
                title=request.json['title'],
                #author_id=request.json['author_id'],
                isbn=request.json['isbn'],
                #genre=request.json['genre'],
                publish_date=request.json['publish_date']
            )
            db.session.add(new_book)
            db.session.commit()

            return '{} created'.format(str(new_book.title)), 201
        except KeyError:
            abort(400)
        except Exception as e:
            print(e)
            abort(404)

    @app.route(make_path('/Books'), methods=['GET'])
    def get_all_books():
        try:
            books = Book.query.filter_by().order_by(Book.id)
            output = [BookSchema().dump(book).data for book in books]
            return jsonify({'book': output}), 200
        except Exception:
            abort(404)

    @app.route(make_path('/Books/<int:book_id>'), methods=['GET'])
    def get_book(book_id):
        try:
            book = Book.query.get(book_id)
            output = BookSchema().dump(book).data
            return jsonify({'book': output}), 200
        except Exception:
            abort(404)

    @app.route(make_path('/Book/<int:book_id>'), methods=['PATCH'])
    def update_book(book_id):
        if not request.json:
            abort(404)
        try:
            book = Book.query.get(book_id)
            title = request.json.get('title', book.title),
            #author_id = request.json.get('author_id', book.author_id),
            isbn = request.json.get('isbn', book.isbn),
            #genre = request.json.get('genre', book.genre),
            publish_date = request.json.get('publish_date', book.publish_date)

            book.title = title
            #book.author_id = author_id
            book.isbn = isbn
            #book.genre = genre
            book.publish_date = publish_date

            db.session.commit()
            return jsonify({'result': 'success'}), 200
        except KeyError:
            abort(400)
        except Exception as e:
            print(e)
            db.session.rollback()
            abort(404)

    @app.route(make_path('/Books/<int:book_id>'), methods=['DELETE'])
    def delete_book(book_id):
        try:
            book = Book.query.get(book_id)
            db.session.delete(book)
            db.session.commit()

            return jsonify({'result': 'success'}), 200
        except Exception:
            db.session.rollback()
            abort(404)

    @app.route(make_path('/Genre'), methods=['GET'])
    def get_all_genre():
        try:
            genres = Genre.query.filter_by().order_by(Genre.id)
            output = [GenreSchema().dump(genre).data for genre in genres]
            if not output:
                return jsonify({'genre': "No Records"})
            return jsonify({'genre': output})
        except Exception as e:
            print(e)
            abort(400)

    @app.route(make_path('/Genre/limit/<int:genre_limit>'), methods=['GET'])
    def get_limited_genres(genre_limit):
        try:
            genres = Genre.query.filter_by().order_by(Genre.id).limit(genre_limit)
            output = [GenreSchema().dump(genre).data for genre in genres]
            if not output:
                return jsonify({'genre': "No Records"})
            return jsonify({'genre': output})
        except Exception as e:
            print(e)
            abort(404)

    @app.route(make_path('/Genre/<int:id>'), methods=['GET'])
    def get_selected_genre(id):
        try:
            genre = Genre.query.get(id)
            output = GenreSchema().dump(genre).data
            return jsonify({'genre': output})
        except Exception as e:
            print(e)
            abort(404)

    @app.route(make_path('/Genre/<int:id>'), methods=['PATCH'])
    def update_genre(id):
        if not request.json:
            abort(400)
        try:
            genre = Genre.query.get(id)
            genre.name = request.json['genre']
            db.session.commit()
            return 'OK', 200
        except KeyError:
            abort(400)
        except Exception as e:
            print(e)
            abort(418)

    @app.route(make_path('/Genre/<int:id>'), methods=['DELETE'])
    def delete_genre(id):
        try:
            genre = Genre.query.get(id)
            db.session.delete(genre)
            db.session.commit()
            return '{} is Deleted'.format(genre.name)
        except KeyError:
            abort(400)
        except Exception as e:
            print(e)
            abort(418)

    @app.route(make_path('/Genre'), methods=['POST'])
    def add_genre():
        if not request.json and 'genre' not in request.json:
            abort(400)
        genre = Genre.query.filter_by(name=request.json['genre']).first()
        if genre and len(genre) > 0:
            return "{} is already exist".format(request.json['genre'])
        new_genre = Genre(name=request.json['genre'])
        db.session.add(new_genre)
        db.session.commit()
        return "{} Created".format(str(new_genre.name)), 201
