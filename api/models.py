from extensions import db


class BookInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    status = db.Column(db.String(30), nullable=False)
    due_back = db.Column(db.Date, nullable=True)


"""
class BookGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

"""


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    #author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
    #                      nullable=False)
    isbn = db.Column(db.String(13), nullable=False)
    #genres = db.relationship('Genre',
    #                         backref=db.backref('books', lazy='dynamic'),
    #                         secondary='book_genre')
    publish_date = db.Column(db.String(10))
    #book_copies = db.relationship('BookInstance', backref='book')

    def __init__(self, title, isbn, publish_date):
        self.title = title
        #self.author_id = author_id
        self.isbn = isbn
        #self.genre = genre
        self.publish_date = publish_date

    def __repr__(self):
        return f'<Book: {self.author_id} {self.publish_date}>'

    def __str__(self):
        return f'{self.author_id} {self.publish_date}'
