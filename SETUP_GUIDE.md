# Coffee Shop Backend - Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
# Option 1: Using the provided runner script
python run_server.py

# Option 2: Traditional Flask way
cd src
set FLASK_APP=api.py
flask run --reload
```

### 3. Populate Database (Optional)
```bash
python populate_db.py
```

### 4. Test the API
```bash
python test_api.py
```

## API Endpoints

### Public Endpoints
- `GET /` - Health check
- `GET /drinks` - Get all drinks (short format)

### Protected Endpoints (Require Authentication)
- `GET /drinks-detail` - Get all drinks (detailed format) - Requires `get:drinks-detail` permission
- `POST /drinks` - Create a new drink - Requires `post:drinks` permission
- `PATCH /drinks/<id>` - Update a drink - Requires `patch:drinks` permission
- `DELETE /drinks/<id>` - Delete a drink - Requires `delete:drinks` permission

## Auth0 Configuration

Update the following variables in `src/auth/auth.py`:
```python
AUTH0_DOMAIN = 'your-domain.auth0.com'
API_AUDIENCE = 'your-api-identifier'
```

### Required Permissions
- `get:drinks-detail` - View detailed drink information
- `post:drinks` - Create new drinks
- `patch:drinks` - Update existing drinks
- `delete:drinks` - Delete drinks

### Roles
- **Barista**: Can view drink details (`get:drinks-detail`)
- **Manager**: Can perform all actions (all permissions)

## Testing with Postman

1. Import the collection: `udacity-fsnd-udaspicelatte.postman_collection.json`
2. Set up environment variables with your JWT tokens
3. Test all endpoints with appropriate permissions

## Sample Drink Format

```json
{
    "title": "Latte",
    "recipe": [
        {
            "name": "Coffee",
            "color": "#8B4513",
            "parts": 1
        },
        {
            "name": "Steamed Milk",
            "color": "#FFFFFF",
            "parts": 3
        }
    ]
}
```

## Error Handling

The API returns standard HTTP status codes:
- `200` - Success
- `401` - Unauthorized (missing or invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Resource not found
- `422` - Unprocessable entity (invalid data)
- `500` - Internal server error

## Development Notes

- Database is automatically initialized on first run
- Use `db_drop_and_create_all()` to reset the database
- All endpoints return JSON responses
- CORS is enabled for cross-origin requests