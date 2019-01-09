from flask import Flask
from routes import create_routes
from extensions import db, ma, migrate

DB_SETTINGS = {
    'user': 'postgres',
    'pw': "",
    'db': 'librarydb',
    'host': 'localhost',
    'port': '5432',
}


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(
        user=DB_SETTINGS['user'],
        pw=DB_SETTINGS['pw'],
        host=DB_SETTINGS['host'],
        port=DB_SETTINGS['port'],
        db=DB_SETTINGS['db']
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    register_extensions(app)
    register_routes(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    return None


def register_routes(app):
    create_routes(app)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
