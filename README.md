# Healthcare Project

A FastAPI-based project designed to manage healthcare-related data, including organizations, user reports, and user tests.

## Project Structure

```
healthcare_project/
├── apps/
│   ├── organizations/         # Handles organization-related data
│   │   ├── __init__.py
│   │   ├── models.py          # SQLAlchemy models for organizations
│   │   ├── schemas.py         # Pydantic schemas for organizations
│   │   ├── crud.py            # CRUD operations for organizations
│   │   ├── routers.py          # API routes for organizations
│   ├── reports/               # Handles user reports and tests
│   │   ├── __init__.py
│   │   ├── models.py          # SQLAlchemy models for reports and tests
│   │   ├── schemas.py         # Pydantic schemas for reports and tests
│   │   ├── crud.py            # CRUD operations for reports and tests
│   │   ├── routers.py          # API routes for reports
│   ├── users/                 # Manages user-related functionality
│   │   ├── __init__.py
│   │   ├── models.py          # SQLAlchemy models for users
│   │   ├── schemas.py         # Pydantic schemas for users
│   │   ├── crud.py            # CRUD operations for users
│   │   ├── routers.py          # API routes for users
├── core/
│   ├── __init__.py
│   ├── database.py            # Database connection and session setup
│   ├── settings.py            # Application configuration
├── migrations/                # Alembic migrations folder
│   ├── env.py
│   ├── README
│   └── versions/              # Migration files
├── main.py                    # Application entry point
├── alembic.ini                # Alembic configuration file
├── mydb.db                     # SQLite database (excluded from Git)
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## Prerequisites

- Python 3.10+
- SQLite (or an alternative database if configured)
- FastAPI
- SQLAlchemy
- Alembic

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/healthcare_project.git
    cd healthcare_project
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure your `.env` file for settings:
    ```env
    DATABASE_URL=sqlite:///./mydb.db
    ```

## Usage

### Running the Application
1. Initialize the database:
    ```bash
    alembic upgrade head
    ```

2. Start the server:
    ```bash
    uvicorn main:app --reload
    ```

3. Visit the API documentation at:
    - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Migrations
1. Generate a new migration:
    ```bash
    alembic revision --autogenerate -m "Migration message"
    ```

2. Apply migrations:
    ```bash
    alembic upgrade head
    ```

### Testing
Run the test suite using pytest:
```bash
pytest
```

## Features

- **Organizations**: Create, update, and delete organization data.
- **User Reports**: Manage user reports and related tests.
- **User Management**: Handle user creation and operations.

## Contributing

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a pull request.
