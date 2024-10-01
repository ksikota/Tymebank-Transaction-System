from flask_restx import Resource, fields
from models import Transaction
from flask import request
from datetime import datetime
from app import db

def register_routes(api):
    # Create a namespace for transactions
    ns = api.namespace('transactions', description='Financial Transactions operations')

    # Define the transaction model for Swagger documentation
    transaction_model = api.model('Transaction', {
        'id': fields.Integer(readOnly=True, description='Unique identifier for the transaction'),
        'type': fields.String(required=True, description='Type of transaction (credit or debit)'),
        'description': fields.String(required=True, description='Transaction description'),
        'date': fields.String(required=True, description='Transaction date in YYYY-MM-DD format'),
        'amount': fields.Float(required=True, description='Amount of the transaction (negative for debit)')
    })

    # Create the transaction routes
    @ns.route('/', strict_slashes=False)  # Add strict_slashes=False here
    class TransactionList(Resource):
        @api.marshal_list_with(transaction_model)
        def get(self):
            """Retrieve all transactions"""
            transactions = Transaction.query.all()
            return transactions

        @api.expect(transaction_model)
        def post(self):
            """Create a new transaction"""
            data = request.json
            new_transaction = Transaction(
                type=data['type'],
                description=data['description'],
                date=datetime.strptime(data['date'], '%Y-%m-%d'),
                amount=data['amount']
            )
            db.session.add(new_transaction)
            db.session.commit()
            return {'message': 'Transaction created successfully'}, 201

    @ns.route('/<int:id>', strict_slashes=False)  # Add strict_slashes=False here
    @api.response(404, 'Transaction not found')
    @api.param('id', 'The transaction identifier')
    class TransactionResource(Resource):
        @api.marshal_with(transaction_model)
        def get(self, id):
            """Retrieve a specific transaction by ID"""
            transaction = Transaction.query.get_or_404(id)
            return transaction

        def delete(self, id):
            """Delete a transaction by ID"""
            transaction = Transaction.query.get_or_404(id)
            db.session.delete(transaction)
            db.session.commit()
            return {'message': 'Transaction deleted successfully'}, 200

        @api.expect(transaction_model)
        def put(self, id):
            """Update a specific transaction by ID"""
            transaction = Transaction.query.get_or_404(id)
            data = request.json
            transaction.type = data['type']
            transaction.description = data['description']
            transaction.date = datetime.strptime(data['date'], '%Y-%m-%d')
            transaction.amount = data['amount']
            db.session.commit()
            return {'message': 'Transaction updated successfully'}, 200

    # Add the namespace to the API
    api.add_namespace(ns)
