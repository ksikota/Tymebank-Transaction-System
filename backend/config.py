import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/financial_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False