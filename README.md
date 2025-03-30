# FastAPI Project

This project is a FastAPI-based application that provides APIs for managing movies and user authentication.

## Getting Started

Follow these steps to set up the project and start contributing.

### Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- `pip` for Python package management

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastAPI

   ```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
   `pip install -r requirements.txt`

4. Run the application locally:
   `uvicorn main:app --reload`

5. Access the application at http://127.0.0.1:8000.

## Folder Structure

The project is organized as follows:

```bash
fastAPI/
├── app/
│ ├── config/ # Configuration files (e.g., database setup)
│ │ ├── __init__.py
│ │ └── database.py
│ ├── middlewares/ # Custom middlewares (e.g., error handling, JWT authentication)
│ │ ├── __init__.py
│ │ ├── error_handler.py
│ │ └── jwt_bearer.py
│ ├── models/ # SQLAlchemy models
│ │ ├── __init__.py
│ │ └── movie.py
│ ├── routers/ # API route definitions
│ │ ├── __init__.py
│ │ ├── movie.py
│ │ └── user.py
│ ├── schemas/ # Pydantic schemas for data validation
│ │ ├── __init__.py
│ │ ├── movie.py
│ │ └── user.py
│ ├── services/ # Business logic and service classes
│ │ ├── __init__.py
│ │ └── movie.py
│ └── tests/ # Unit tests
│ ├── __init__.py
│ └── test_movie.py
├── main.py # Application entry point
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── Makefile # Makefile for common commands
```

### Docker Setup

You can use Docker to containerize and run the application.

Build the Docker Image
`docker build -t fastapi .`
Run the Docker Container
`docker run --name fastapi -p 5000:5000 -v ${PWD}:/app -d fastapi`
Stop the Docker Container
`docker stop fastapi`
Access logs
`docker logs fastapi -f`

### Running tests

To run tests, use the following commands
`pytest -s app/`

### Contributing

1. Fork the repository
2. Create a new branch for your feature or bug fix:
   `git checkout -b feature/<issue-id>-<feature-name>`
3. Commit your changes:
   `git commit -m "feat: description for changes"`
4. Push your branch:
   `git push origin feature/<issue-id>-<feature-name>`
5. Open a pull request.

License
This project is licensed under the MIT License.
