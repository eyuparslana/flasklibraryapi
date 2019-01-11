from extensions import ma
from models import BookInstance, Book, Genre


class BookInstanceSchema(ma.ModelSchema):
    class Meta:
        model = BookInstance


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book


class GenreSchema(ma.ModelSchema):
    class Meta:
        model = Genre

