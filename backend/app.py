from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restx import Api
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Initialize Swagger-RESTX
api = Api(version="1.0", title="Financial Transaction API", description="API for managing financial transactions")


def create_app():
    app = Flask(__name__)
    # Allow cross-origin requests from the specific origin (localhost:63342)
    # CORS(app, resources={r"/*": {"origins": "http://localhost:63342"}})
    CORS(app, resources={r"/*": {"origins": "*"}})
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/financial_db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)  # Initialize the RESTX API with the Flask app

    # Import models here to avoid circular import
    with app.app_context():
        from models import Transaction  # Import models inside the app context

    # Register routes
    from routes import register_routes  # Register the routes from routes.py
    register_routes(api)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=4999)
