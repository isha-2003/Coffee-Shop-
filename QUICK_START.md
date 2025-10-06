# Quick Start Guide - Coffee Shop App

Get your Coffee Shop application running in 4 simple phases.

---

## Prerequisites

- Python 3.7+ installed
- Node.js 14-16 installed (or 17+ with workaround)
- Text editor
- Web browser
- 45-60 minutes of your time

---

## Phase 1: Auth0 Setup (30 minutes)

### What you'll do:
Set up Auth0 for authentication and authorization.

### Steps:
1. Go to https://auth0.com and create a free account
2. Create a Single Page Application named "Coffee Shop"
3. Create an API with identifier `coffee` and add 4 permissions
4. Create 2 roles: Barista and Manager
5. Create 2 test users and assign roles

### What you'll get:
- Auth0 Domain (e.g., `dev-abc123.us.auth0.com`)
- Client ID (long string)

### Detailed instructions:
See **CONFIGURATION_STEPS.md** sections 1-5

---

## Phase 2: Configure App (10 minutes)

### What you'll do:
Update configuration files with your Auth0 credentials.

### Files to update:

#### 1. `src/environments/environment.ts`
```typescript
auth0: {
  url: 'dev-abc123',              // Your tenant prefix
  audience: 'coffee',             // Keep as is
  clientId: 'YOUR_CLIENT_ID',     // Your Client ID
  callbackURL: 'http://localhost:8100',
}
```

#### 2. `src/auth/auth.py`
```python
AUTH0_DOMAIN = 'dev-abc123.us.auth0.com'  # Your full domain
API_AUDIENCE = 'coffee'                    # Keep as is
```

### Quick reference:
See **AUTH0_QUICK_REFERENCE.md** for examples

---

## Phase 3: Install & Run (10 minutes)

### What you'll do:
Install dependencies and start the application.

### Commands:

```bash
# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
npm install

# Terminal 1: Start backend
python run_server.py

# Terminal 2: Start frontend (in new terminal)
npm start
# OR if Node 17+: export NODE_OPTIONS=--openssl-legacy-provider && npm start

# Optional: Populate database with sample drinks
python populate_db.py
```

### What you'll see:
- Backend running on http://127.0.0.1:5000
- Frontend running on http://localhost:8100

### Detailed instructions:
See **START_APP.md**

---

## Phase 4: Test (10 minutes)

### What you'll do:
Test the application with both user roles.

### Test as Barista:
1. Open http://localhost:8100
2. Click User tab → Log In
3. Login: `barista@coffeeshop.com` / `Test123!`
4. Go to Drink Menu
5. Verify: Can view drinks, NO "Create Drink" button

### Test as Manager:
1. Click Log Out
2. Click Log In
3. Login: `manager@coffeeshop.com` / `Test123!`
4. Go to Drink Menu
5. Verify: Can see "Create Drink" button
6. Click "Create Drink" and add a new drink
7. Click a drink to edit/delete it

---

## Success Criteria

Your setup is complete when:
- ✓ Both users can login
- ✓ Barista can only view drinks
- ✓ Manager can create/edit/delete drinks
- ✓ No errors in browser console
- ✓ No errors in terminal

---

## Common Issues

### Can't login
**Fix**: Double-check Auth0 domain and Client ID in config files

### "Permission denied" errors
**Fix**: Verify roles are assigned to users in Auth0 Dashboard

### Build errors with Node.js
**Fix**: Use Node.js 14-16, or add `export NODE_OPTIONS=--openssl-legacy-provider`

### No drinks showing
**Fix**: Run `python populate_db.py`

---

## Need More Help?

| Issue | Documentation |
|-------|---------------|
| Detailed Auth0 setup | CONFIGURATION_STEPS.md |
| Configuration examples | AUTH0_QUICK_REFERENCE.md |
| Visual diagrams | VISUAL_GUIDE.md |
| Progress tracking | SETUP_CHECKLIST.md |
| Complete overview | COMPLETE_SETUP_SUMMARY.md |

---

## Test Credentials

| Role | Email | Password |
|------|-------|----------|
| Barista | barista@coffeeshop.com | Test123! |
| Manager | manager@coffeeshop.com | Test123! |

---

## What's Next?

After successful setup:
1. Experiment with creating custom drinks
2. Review the code to understand Auth0 integration
3. Check JWT tokens in the User tab
4. Explore the API with Postman

---

## Quick Commands Reference

```bash
# Start backend
python run_server.py

# Start frontend (Node 14-16)
npm start

# Start frontend (Node 17+)
export NODE_OPTIONS=--openssl-legacy-provider && npm start

# Populate database
python populate_db.py

# Test API
python test_api.py
```

---

**Ready to start?** Begin with Phase 1 and follow the steps in order. Good luck!
