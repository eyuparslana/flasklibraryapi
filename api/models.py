from extensions import db


class BookInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    status = db.Column(db.String(30), nullable=False)
    due_back = db.Column(db.Date, nullable=True)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return {'id': self.id, 'name': self.name}

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return '{}'.format(self.name)
