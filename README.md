# Coffee Shop App - Uda-Spice Latte

A full-stack coffee shop application demonstrating Role-Based Access Control (RBAC) using Auth0, Flask, and Ionic/Angular.

## Overview

This application showcases professional authentication and authorization patterns:
- **OAuth 2.0** authentication via Auth0
- **JWT (JSON Web Token)** based API security
- **Role-Based Access Control** with Barista and Manager roles
- **RESTful API** with Flask backend
- **Modern UI** with Ionic/Angular frontend

### User Roles

- **Barista**: Can view drink details only
- **Manager**: Can create, edit, and delete drinks (full access)

## Quick Start

**Want to get started fast?** See **[QUICK_START.md](QUICK_START.md)** for a condensed 4-phase setup guide.

### New to this project? Start here:

1. **[QUICK_START.md](QUICK_START.md)** - Fast-track setup guide (45-60 minutes)
2. **[COMPLETE_SETUP_SUMMARY.md](COMPLETE_SETUP_SUMMARY.md)** - High-level overview of the entire setup process
3. **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Visual walkthrough with diagrams and flowcharts
4. **[SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)** - Printable checklist to track your progress

### Detailed Setup Guides:

1. **[CONFIGURATION_STEPS.md](CONFIGURATION_STEPS.md)** - Complete step-by-step Auth0 and application setup
2. **[AUTH0_QUICK_REFERENCE.md](AUTH0_QUICK_REFERENCE.md)** - Quick reference for Auth0 configuration values
3. **[START_APP.md](START_APP.md)** - How to start the application after configuration

## Prerequisites

- Python 3.7+
- Node.js 14-16 (recommended) or 17+ with legacy OpenSSL provider
- Auth0 account (free tier is sufficient)
- npm or yarn

## Installation

### 1. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Frontend Dependencies
```bash
npm install
```

### 3. Configure Auth0
Follow the detailed instructions in [CONFIGURATION_STEPS.md](CONFIGURATION_STEPS.md) to:
- Create Auth0 account and application
- Set up API with permissions
- Create roles (Barista, Manager)
- Create test users

### 4. Update Configuration Files
Update these files with your Auth0 credentials (see [AUTH0_QUICK_REFERENCE.md](AUTH0_QUICK_REFERENCE.md)):
- `src/environments/environment.ts` (Frontend)
- `src/auth/auth.py` (Backend)

## Running the Application

### Start Backend (Terminal 1)
```bash
python run_server.py
```
Backend will run on http://127.0.0.1:5000

### Start Frontend (Terminal 2)

For Node.js 14-16:
```bash
npm start
```

For Node.js 17+:
```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm start
```

Frontend will run on http://localhost:8100

## Test Credentials

| Role | Email | Password | Permissions |
|------|-------|----------|-------------|
| Barista | barista@coffeeshop.com | Test123! | View drinks only |
| Manager | manager@coffeeshop.com | Test123! | Full access |

## API Endpoints

| Method | Endpoint | Permission | Description |
|--------|----------|------------|-------------|
| GET | /drinks | Public | Get all drinks (short format) |
| GET | /drinks-detail | get:drinks-detail | Get all drinks (detailed) |
| POST | /drinks | post:drinks | Create a new drink |
| PATCH | /drinks/\<id\> | patch:drinks | Update a drink |
| DELETE | /drinks/\<id\> | delete:drinks | Delete a drink |

## Project Structure

```
coffee-shop-app/
├── src/
│   ├── api.py                 # Flask API routes
│   ├── auth/
│   │   └── auth.py           # Auth0 JWT validation
│   ├── database/
│   │   ├── models.py         # Database models
│   │   └── database.db       # SQLite database
│   ├── app/                  # Angular/Ionic frontend
│   │   ├── services/         # Auth and API services
│   │   └── pages/            # App pages (drink menu, user)
│   └── environments/
│       └── environment.ts    # Frontend configuration
├── populate_db.py            # Script to add sample drinks
├── run_server.py             # Backend startup script
└── get_token.html           # Helper to get JWT tokens
```

## Documentation

### Getting Started Guides
- **[QUICK_START.md](QUICK_START.md)** - Fast-track 4-phase setup guide
- **[COMPLETE_SETUP_SUMMARY.md](COMPLETE_SETUP_SUMMARY.md)** - Overview and big picture
- **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - Visual walkthrough with diagrams
- **[SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)** - Progress tracking checklist

### Configuration Guides
- **[CONFIGURATION_STEPS.md](CONFIGURATION_STEPS.md)** - Detailed setup instructions
- **[AUTH0_QUICK_REFERENCE.md](AUTH0_QUICK_REFERENCE.md)** - Configuration values reference
- **[AUTH0_CONFIG.md](AUTH0_CONFIG.md)** - Auth0 configuration checklist

### Running & Testing
- **[START_APP.md](START_APP.md)** - Running the application
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Backend setup guide

## Technologies Used

### Backend
- Flask - Web framework
- SQLAlchemy - ORM
- Flask-CORS - Cross-Origin Resource Sharing
- python-jose - JWT validation
- Auth0 - Authentication and authorization

### Frontend
- Ionic 4 - UI framework
- Angular 7 - Frontend framework
- TypeScript - Programming language
- @auth0/angular-jwt - JWT handling

## Features

- Secure authentication with Auth0
- Role-based permission system
- JWT token validation
- Visual drink builder with recipe editor
- Real-time permission-based UI updates
- RESTful API design
- Responsive mobile-first design

## Troubleshooting

See [CONFIGURATION_STEPS.md](CONFIGURATION_STEPS.md) for detailed troubleshooting guide.

Common issues:
- **Login not working**: Check Auth0 configuration
- **Permission errors**: Verify roles assigned to users
- **Build errors**: Use Node.js 14-16 or legacy provider
- **No drinks showing**: Run `python populate_db.py`

## Testing

### Test API Endpoints
```bash
python test_api.py
```

### Populate Sample Data
```bash
python populate_db.py
```

## Reference

This project is based on the Udacity Full Stack Nanodegree Coffee Shop project, demonstrating enterprise-level authentication and authorization patterns.

**Reference Video**: https://www.youtube.com/watch?v=cUtS2DJQJ7I

## License

This project is for educational purposes as part of the Udacity Full Stack Nanodegree program.  
