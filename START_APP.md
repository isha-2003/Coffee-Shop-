# How to Start the Coffee Shop Application

Follow these simple steps to run your application.

---

## Prerequisites

Before starting, make sure you have:
1. Completed Auth0 setup (see `CONFIGURATION_STEPS.md`)
2. Updated configuration files with your Auth0 credentials
3. Installed Python dependencies: `pip install -r requirements.txt`
4. Installed Node dependencies: `npm install`

---

## Starting the Application

### Terminal 1: Start Backend (Flask API)

```bash
python run_server.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

**Keep this terminal running!**

---

### Terminal 2: Start Frontend (Ionic App)

**For Node.js 14-16:**
```bash
npm start
```

**For Node.js 17+:**
```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm start
```

Or alternatively:
```bash
ionic serve
```

You should see:
```
[ng] ** Angular Live Development Server is listening on localhost:8100 **
```

**Keep this terminal running!**

---

## Access the Application

1. Open your browser
2. Go to: `http://localhost:8100`
3. You should see the Coffee Shop app with tabs at the bottom

---

## Testing the App

### Test as Barista (View Only)

1. Click the **User** tab
2. Click **Log In**
3. Login with:
   - Email: `barista@coffeeshop.com`
   - Password: `Test123!`
4. Go to **Drink Menu** tab
5. You can view drinks but cannot create/edit/delete

### Test as Manager (Full Access)

1. Click **Log Out** in the User tab
2. Click **Log In** again
3. Login with:
   - Email: `manager@coffeeshop.com`
   - Password: `Test123!`
4. Go to **Drink Menu** tab
5. You can create, view, edit, and delete drinks

---

## Stopping the Application

1. In Terminal 1 (Backend): Press `Ctrl+C`
2. In Terminal 2 (Frontend): Press `Ctrl+C`

---

## Troubleshooting

### Backend won't start
- Check if port 5000 is already in use
- Verify Python dependencies are installed
- Check database file exists: `src/database/database.db`

### Frontend won't start
- Check if port 8100 is already in use
- Verify Node.js version (14-16 recommended)
- Try clearing node_modules and reinstalling: `rm -rf node_modules && npm install`

### Login not working
- Verify Auth0 configuration in `environment.ts` and `auth.py`
- Check Auth0 Dashboard callback URLs
- Look for errors in browser console (F12)

### No drinks showing
- Run `python populate_db.py` to add sample drinks
- Check browser console for API errors
- Verify backend is running on port 5000

---

## Quick Commands Reference

| Task | Command |
|------|---------|
| Start Backend | `python run_server.py` |
| Start Frontend (Node 14-16) | `npm start` |
| Start Frontend (Node 17+) | `export NODE_OPTIONS=--openssl-legacy-provider && npm start` |
| Populate Database | `python populate_db.py` |
| Test API | `python test_api.py` |
| Stop Server | `Ctrl+C` |

---

## Application Structure

```
Coffee Shop App
├── Backend (Flask) - http://127.0.0.1:5000
│   ├── GET /drinks - Public endpoint
│   ├── GET /drinks-detail - Requires auth
│   ├── POST /drinks - Manager only
│   ├── PATCH /drinks/<id> - Manager only
│   └── DELETE /drinks/<id> - Manager only
│
└── Frontend (Ionic/Angular) - http://localhost:8100
    ├── Drink Menu Tab - View/manage drinks
    └── User Tab - Login/logout
```

---

## Next Steps

Once the app is running:
1. Test both user roles to see permission differences
2. Try creating a new drink as Manager
3. Try editing an existing drink
4. Log in as Barista and verify you can only view
5. Explore the JWT token in the User page

Enjoy your Coffee Shop application!
