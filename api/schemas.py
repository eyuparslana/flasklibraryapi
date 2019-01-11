from extensions import ma
from models import BookInstance, Book


class BookInstanceSchema(ma.ModelSchema):
    class Meta:
        model = BookInstance

class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book

