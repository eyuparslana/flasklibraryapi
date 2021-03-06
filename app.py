from flask import Blueprint
from flask_restful import Api
from resources.Author import AuthorResource, AuthorListResource
from resources.Author import AuthorSearchResource
from resources.Book import BookResource, BookListResource, BookSearchResource
from resources.BookInstance import BookInstanceResource, BookInstanceListResource
from resources.Genre import GenreResource, GenreListResource
from resources.Loan import LoanResource, LoanReturnResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(AuthorListResource, '/Author')
api.add_resource(AuthorSearchResource, '/Author/Search')
api.add_resource(AuthorResource, '/Author/<author_id>')

api.add_resource(BookListResource, '/Book')
api.add_resource(BookResource, '/Book/<book_id>')
api.add_resource(BookSearchResource, '/Book/Search')

api.add_resource(BookInstanceListResource, '/BookInstance')
api.add_resource(BookInstanceResource, '/BookInstance/<book_instance_id>')

api.add_resource(GenreListResource, '/Genre')
api.add_resource(GenreResource, '/Genre/<genre_id>')

api.add_resource(LoanResource, '/Loan')
api.add_resource(LoanReturnResource, '/Loan/<loan_id>')
