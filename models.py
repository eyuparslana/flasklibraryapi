from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'Genre={self.name}'


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'Author={self.first_name} {self.last_name}'


class BookGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'authors.id', ondelete='CASCADE'), nullable=False)
    author = db.relationship(
        'Author',
        backref=db.backref('books', lazy='dynamic'))
    genres = db.relationship(
        'Genre',
        secondary='book_genre',
        backref=db.backref('books', lazy='dynamic'))

    def __str__(self):
        return f'Book={self.title}'


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


class BaseSchema(ma.ModelSchema):
    class Meta:
        sqla_session = db.session


class GenreSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Genre


class AuthorSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Author


class BookSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Book
    author_id = fields.Integer(required=True)


class BookInstanceSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = BookInstance
    book_id = fields.Integer(required=True)

