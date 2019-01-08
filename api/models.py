from extensions import db


class BookInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    status = db.Column(db.String(30), nullable=False)
    due_back = db.Column(db.Date, nullable=True)
