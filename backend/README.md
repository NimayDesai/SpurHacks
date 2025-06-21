# SpurHacks Backend

This is a Flask-based RESTful API backend for the SpurHacks project. It provides endpoints for user authentication including signup, login, and logout.

## Setup

1. Make sure you have Python 3.7+ installed
2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Running the server

You can run the server using the provided script:

```bash
./run.sh
```

Or manually:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python main.py
```

The server will start on http://localhost:5000

## API Endpoints

### Authentication

- **POST /api/auth/signup** - Register a new user

  - Request body: `{ "username": "user", "email": "user@example.com", "password": "password" }`
  - Response: `{ "message": "User created successfully", "user": {...} }`

- **POST /api/auth/login** - Log in a user

  - Request body: `{ "username": "user", "password": "password" }`
  - Response: `{ "message": "Login successful", "user": {...}, "access_token": "..." }`

- **POST /api/auth/logout** - Log out a user (requires JWT token)

  - Headers: `Authorization: Bearer <token>`
  - Response: `{ "message": "Logout successful" }`

- **GET /api/auth/me** - Get current user info (requires JWT token)
  - Headers: `Authorization: Bearer <token>`
  - Response: `{ "user": {...} }`
