from app import db  # Ensure this import remains the same


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # credit or debit
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'date': self.date.strftime('%Y-%m-%d'),
            'amount': self.amount
        }
