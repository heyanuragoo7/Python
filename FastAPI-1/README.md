# FastAPI MongoDB Tutorial

This is a simple FastAPI application demonstrating CRUD operations with MongoDB.

## Features

- **MongoDB Database**: Using Beanie ODM
- **User Signup**: Create new user accounts
- **User Login**: JWT token authentication
- **CRUD Operations**: Create, Read, Update, Delete users
- **Async Operations**: Asynchronous database operations
- **Background Tasks**: Email sending and logging
- **Middleware**: Request logging
- **Exception Handling**: Custom error responses

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up MongoDB**:
   - Install MongoDB locally or use MongoDB Atlas
   - Update `MONGODB_URL` in `database.py` if needed
   - Default: `mongodb://localhost:27017/fastapi_db`

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API documentation**:
   - Open http://127.0.0.1:8000/docs for interactive Swagger UI

## API Endpoints

### Public Endpoints
- `GET /` - Welcome message
- `POST /signup` - Create new user account
- `POST /login` - Login and get JWT token
- `GET /users` - List all users (with pagination and search)
- `GET /async-example` - Async operation example
- `POST /send-email` - Background task example

### Protected Endpoints (require JWT token)
- `GET /me` - Get current user profile
- `GET /users/{user_id}` - Get specific user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Usage Examples

### 1. Signup
```bash
curl -X POST "http://127.0.0.1:8000/signup" \
     -H "Content-Type: application/json" \
     -d '{"username": "john", "email": "john@example.com", "password": "secret"}'
```

### 2. Login
```bash
curl -X POST "http://127.0.0.1:8000/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "john", "password": "secret"}'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Get Users
```bash
curl "http://127.0.0.1:8000/users?skip=0&limit=5&search=john"
```

### 4. Access Protected Endpoint
```bash
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     "http://127.0.0.1:8000/me"
```

### 5. Update User
```bash
curl -X PUT "http://127.0.0.1:8000/users/YOUR_USER_ID" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"username": "john_updated"}'
```

## Key Concepts

- **Beanie ODM**: Object Document Mapper for MongoDB
- **Async Operations**: Non-blocking database operations
- **JWT Authentication**: Secure token-based auth
- **Pydantic Validation**: Automatic data validation
- **Background Tasks**: Operations that run after response
- **Middleware**: Code that runs on every request</content>
<parameter name="filePath">d:\Workspace\Engage-In\fastapi-1\README.md