from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.secret_key = 'some secret key'

    from models import db, Author, Book, BookInstance, Genre, Loan
    db.init_app(app)
    admin = Admin(app)
    admin.add_view(ModelView(Author, db.session))
    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(BookInstance, db.session))
    admin.add_view(ModelView(Genre, db.session))
    admin.add_view(ModelView(Loan, db.session))

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
