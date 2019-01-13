from flask import Blueprint
from flask_restful import Api
from resources.Author import AuthorResource, AuthorListResource
from resources.Book import BookResource, BookListResource
from resources.BookInstance import BookInstanceResource, BookInstanceListResource
from resources.Genre import GenreResource, GenreListResource
from resources.Catalog import CatalogResource, CatalogReturnResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(AuthorListResource, '/Author')
api.add_resource(AuthorResource, '/Author/<author_id>')

api.add_resource(BookListResource, '/Book')
api.add_resource(BookResource, '/Book/<book_id>')

api.add_resource(BookInstanceListResource, '/BookInstance')
api.add_resource(BookInstanceResource, '/BookInstance/<book_instance_id>')

api.add_resource(GenreListResource, '/Genre')
api.add_resource(GenreResource, '/Genre/<genre_id>')

api.add_resource(CatalogResource, '/Catalog')
api.add_resource(CatalogReturnResource, '/Catalog/<loan_id>')
