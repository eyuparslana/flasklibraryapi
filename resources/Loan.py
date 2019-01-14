from flask import request
from flask_restful import Resource
from models import db, Book, Loan, LoanSchema
from datetime import datetime, timedelta

loans_schema = LoanSchema(many=True)
loan_schema = LoanSchema()


class LoanResource(Resource):
    def get(self):
        '''GET method to list all loans'''

        loans = Loan.query.all()

        result = loans_schema.dump(loans).data
        return {'status': 'success', 'data': result}, 201

    def post(self):
        '''POST method to rent a book instance'''

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            book_id = int(json_data['book_id'])
            loaned_by = str(json_data['loaned_by'])
        except Exception as err:
            return {'message': err}, 400

        # Check book exists
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book does not exist'}, 400

        # Check for available instance
        available_instance = None
        for instance in book.instances:
            if instance.status == 'available':
                available_instance = instance
                break
        if not available_instance:
            return {'message': 'There is no available copy of the book'}, 400

        due_back = datetime.now() + timedelta(days=15)
        available_instance.status = 'on_loan'
        available_instance.due_back = due_back

        loan = Loan(
            book_instance=available_instance,
            loaned_by=loaned_by
        )

        db.session.add(loan)
        db.session.commit()

        result = loan_schema.dump(loan).data
        return {'status': 'success', 'data': result}, 201


class LoanReturnResource(Resource):
    def get(self, loan_id):
        '''GET method to update a book instance to loanable again'''

        loan = Loan.query.get(loan_id)
        if not loan:
            return {'message': 'Loan does not exist'}, 400

        if not loan.is_active:
            return {'message': 'Loan is not active'}, 400

        loan.book_instance.status = 'available'
        loan.book_instance.due_back = None
        loan.is_active = False
        db.session.commit()

        return {'status': 'success'}, 200
