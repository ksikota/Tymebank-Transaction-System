import unittest
from app import create_app, db
from models import Transaction

class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a test client and a new database for each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Create all tables

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()  # Drop all tables

    def test_integration(self):
        """Integration test for adding and retrieving transactions."""
        # Create a new transaction
        response = self.client.post('/transactions', json={
            'type': 'credit',
            'description': 'Test transaction',
            'date': '2023-09-27',
            'amount': 100.00
        })

        self.assertEqual(response.status_code, 201)

        # Retrieve transactions
        response = self.client.get('/transactions')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)  # Expecting one transaction
        self.assertEqual(response.json[0]['description'], 'Test transaction')  # Check transaction description

if __name__ == '__main__':
    unittest.main()
