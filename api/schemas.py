from extensions import ma
from models import BookInstance, Genre


class BookInstanceSchema(ma.ModelSchema):
    class Meta:
        model = BookInstance

class GenreSchema(ma.ModelSchema):
    class Meta:
        model = Genre
