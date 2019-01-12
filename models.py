from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Genre(db.Model):
    __tablename__ = 'genres'

    pass


class Author(db.Model):
    __tablename__ = 'authors'

    pass


class BookGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))


class Book(db.Model):
    __tablename__ = 'books'

    pass


class BookInstance(db.Model):
    __tablename__ = 'book_instances'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    due_back = db.Column(db.Date)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'books.id', ondelete='CASCADE'), nullable=False)
    book = db.relationship(
        'Book',
        backref=db.backref('instances', lazy='dynamic'))

    def __str__(self):
        return f'Book={self.book.__str__} Status={self.status}'


class GenreSchema(ma.Schema):
    pass


class AuthorSchema(ma.Schema):
    pass


class BookSchema(ma.Schema):
    pass


class BookInstanceSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    status = fields.String(required=True, validate=validate.Length(1))
    due_back = fields.Date()
    book_id = fields.Integer(required=True)
