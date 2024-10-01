# Tymebank-Transaction-System
 A simple financial records entry system

## Overview
A simple financial transaction management system that allows a user to view account balances, and manage transactions (credits and debits).

## Features
- Add, view, update, and delete transactions
- Responsive user interface
- Transaction history and account balance calculation
- API documentation using Swagger UI

## Technologies Used
- **Front-end**: HTML, CSS, JavaScript
- **Back-end**: Python, Flask, Flask-RESTX, Flask-CORS
- **Database**: PostgreSQL
- **Environment**: Docker (for database setup)

## Getting Started

### Prerequisites
- Python 3.6 or higher
- PostgreSQL
- Node.js (if using any frontend build tools)
- Docker (for database setup)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ksikota/Tymebank-Transaction-System.git
   
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
2.  Install dependancies
      ```bash
    pip install -r requirements.txt
3. install postgresql:
    ```bash
    brew install postgresql
4. Ensure it's properly installed by checking the version:
   ```bash
    postgres --version
5. Install Docker
   ```bash
    https://www.docker.com/
6. Run the following command in your terminal to pull and start a PostgreSQL container:
    ```bash
   docker run --name financial-db -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -e POSTGRES_DB=financial_db -p 5432:5432 -d postgres
7. First, initialize the migration environment:
   ```bash
    flask db init
8. Create an initial migration script:
    ```bash
   flask db migrate -m "Initial migration"
9. Apply the migration to the database:
   ```bash
    flask db upgrade
10. For the swagger view navigate to 
    ```bash
    http://localhost:4999/
11. For the swagger json view navigate to
    ```bash
    http://127.0.0.1:4999/swagger.json
12. Run the Flask python server run:
    ```bash
    python app.py
13. To run the Frontend of the App run:
    ```bash
     frontend/index.html
14. run unit tests in the "backend" directory
    ```bash
    python -m unittest discover -s tests
