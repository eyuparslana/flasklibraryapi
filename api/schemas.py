from extensions import ma
from models import BookInstance


class BookInstanceSchema(ma.ModelSchema):
    class Meta:
        model = BookInstance
