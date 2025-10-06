# Coffee Shop App - Complete Setup Summary

This document provides a high-level overview of what needs to be done to get your Coffee Shop application running exactly as shown in the Udacity reference video.

---

## What is This Application?

A Coffee Shop management system demonstrating **Role-Based Access Control (RBAC)** using Auth0:
- **Baristas** can view drink details
- **Managers** can create, edit, and delete drinks
- Built with Flask (backend) and Ionic/Angular (frontend)

---

## Complete Setup Process

### Phase 1: Auth0 Configuration (20-30 minutes)

Follow the detailed guide in `CONFIGURATION_STEPS.md` to:

1. **Create Auth0 Account**
   - Sign up at https://auth0.com
   - Create a tenant (your domain)

2. **Create Single Page Application**
   - Create an app in Auth0 Dashboard
   - Configure callback URLs
   - Get Domain and Client ID

3. **Create API**
   - Create "Coffee Shop API" with identifier `coffee`
   - Add permissions: `get:drinks-detail`, `post:drinks`, `patch:drinks`, `delete:drinks`
   - Enable RBAC

4. **Create Roles**
   - Barista role: `get:drinks-detail` permission
   - Manager role: all permissions

5. **Create Test Users**
   - barista@coffeeshop.com (Barista role)
   - manager@coffeeshop.com (Manager role)

### Phase 2: Configure Application (5-10 minutes)

Use `AUTH0_QUICK_REFERENCE.md` for quick configuration:

1. **Update Frontend**: `src/environments/environment.ts`
   - Set Auth0 domain prefix
   - Set Client ID
   - Keep audience as `coffee`

2. **Update Backend**: `src/auth/auth.py`
   - Set full Auth0 domain
   - Keep API_AUDIENCE as `coffee`

3. **Update Token Helper** (Optional): `get_token.html`
   - Set Auth0 domain and Client ID

### Phase 3: Run Application (5 minutes)

Use `START_APP.md` for simple startup instructions:

1. **Install Dependencies**
   ```bash
   # Backend
   pip install -r requirements.txt

   # Frontend
   npm install
   ```

2. **Start Backend**
   ```bash
   python run_server.py
   ```

3. **Start Frontend**
   ```bash
   npm start
   # or with Node 17+: export NODE_OPTIONS=--openssl-legacy-provider && npm start
   ```

4. **Access App**: http://localhost:8100

---

## Document Guide

| Document | Purpose | When to Use |
|----------|---------|-------------|
| **CONFIGURATION_STEPS.md** | Complete step-by-step Auth0 setup | First time setup, detailed instructions |
| **AUTH0_QUICK_REFERENCE.md** | Quick config values reference | When filling in configuration files |
| **START_APP.md** | How to run the application | Every time you start the app |
| **COMPLETE_SETUP_SUMMARY.md** | This file - overview | To understand the big picture |

---

## Configuration Files to Update

You need to update these 3 files with your Auth0 credentials:

1. `src/environments/environment.ts` (Frontend config)
2. `src/auth/auth.py` (Backend config)
3. `get_token.html` (Optional - for testing)

---

## Test Credentials

| Role | Email | Password | Can Do |
|------|-------|----------|--------|
| **Barista** | barista@coffeeshop.com | Test123! | View drinks only |
| **Manager** | manager@coffeeshop.com | Test123! | Create/edit/delete drinks |

---

## Expected Application Behavior

### As Barista:
- Can see all drinks in Drink Menu
- Can click on drinks to view details
- **Cannot** see "Create Drink" button
- **Cannot** edit or delete drinks

### As Manager:
- Can see all drinks in Drink Menu
- Can see "Create Drink" button
- Can click on drinks to edit them
- Can delete drinks
- Full access to all features

---

## Common Issues & Solutions

### Issue: Login not working
**Solution**: Double-check Auth0 configuration in both frontend and backend files

### Issue: "Permission denied" errors
**Solution**: Verify roles are assigned to users in Auth0 Dashboard

### Issue: Build errors with Node.js
**Solution**: Use Node.js 14-16, or use legacy OpenSSL provider for Node 17+

### Issue: No drinks showing
**Solution**: Run `python populate_db.py` to add sample drinks

### Issue: CORS errors
**Solution**: Verify callback URLs are correct in Auth0 Dashboard

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                   Auth0                          │
│  - User Authentication                           │
│  - Role Management (Barista/Manager)            │
│  - Permission Management                         │
│  - JWT Token Generation                          │
└─────────────────────────────────────────────────┘
                       ↓ JWT Token
┌─────────────────────────────────────────────────┐
│              Frontend (Ionic/Angular)            │
│  - Port: 8100                                    │
│  - User Interface                                │
│  - Role-based UI (shows/hides features)         │
│  - Sends JWT with API requests                  │
└─────────────────────────────────────────────────┘
                       ↓ HTTP + JWT
┌─────────────────────────────────────────────────┐
│              Backend (Flask API)                 │
│  - Port: 5000                                    │
│  - Validates JWT tokens                          │
│  - Checks permissions                            │
│  - Database operations (SQLite)                  │
└─────────────────────────────────────────────────┘
```

---

## Endpoints Overview

| Method | Endpoint | Permission Required | Description |
|--------|----------|---------------------|-------------|
| GET | /drinks | None (Public) | Get all drinks (short format) |
| GET | /drinks-detail | get:drinks-detail | Get all drinks (detailed) |
| POST | /drinks | post:drinks | Create a new drink |
| PATCH | /drinks/<id> | patch:drinks | Update a drink |
| DELETE | /drinks/<id> | delete:drinks | Delete a drink |

---

## Quick Start Checklist

- [ ] Auth0 account created
- [ ] Auth0 Application created (Single Page App)
- [ ] Auth0 API created with identifier `coffee`
- [ ] Permissions added to API
- [ ] RBAC enabled in API settings
- [ ] Barista role created with `get:drinks-detail` permission
- [ ] Manager role created with all permissions
- [ ] Test users created (barista and manager)
- [ ] Roles assigned to users
- [ ] `environment.ts` updated with Auth0 domain and client ID
- [ ] `auth.py` updated with Auth0 domain
- [ ] Python dependencies installed
- [ ] Node dependencies installed
- [ ] Backend running on port 5000
- [ ] Frontend running on port 8100
- [ ] Tested login as both roles

---

## Support Resources

1. **Auth0 Documentation**: https://auth0.com/docs
2. **Flask Documentation**: https://flask.palletsprojects.com/
3. **Ionic Documentation**: https://ionicframework.com/docs
4. **Angular Documentation**: https://angular.io/docs

---

## Success Criteria

Your application is correctly set up when:
1. You can login as both Barista and Manager
2. Barista can view drinks but not create/edit/delete
3. Manager can create, edit, and delete drinks
4. The "Create Drink" button only shows for Manager
5. JWT tokens are displayed in the User page
6. No console errors in browser or terminal

---

## Troubleshooting Flow

```
Problem: Can't login
├─> Check: Auth0 configuration in environment.ts and auth.py
├─> Check: Callback URLs in Auth0 Dashboard
└─> Check: Browser console for errors

Problem: Login works but permissions wrong
├─> Check: Roles assigned to users in Auth0
├─> Check: Permissions added to roles
├─> Check: RBAC enabled in API settings
└─> Check: "Add Permissions in Token" enabled

Problem: API calls failing
├─> Check: Backend is running on port 5000
├─> Check: CORS is enabled
├─> Check: JWT token is being sent
└─> Check: Backend logs for errors
```

---

## Next Steps After Setup

1. **Test the application** with both user roles
2. **Explore the code** to understand how Auth0 integration works
3. **Customize the drinks** by creating new ones as Manager
4. **Experiment with permissions** by creating new roles in Auth0
5. **Review JWT tokens** in the User page to see how permissions are encoded

---

## Important Notes

- This application uses Auth0's free tier, which is sufficient for development and testing
- The SQLite database is stored in `src/database/database.db`
- JWT tokens expire after a certain time (configured in Auth0)
- The application demonstrates RBAC but uses a simple database for drinks
- For production use, consider using PostgreSQL instead of SQLite
- Always keep your Auth0 credentials secure and never commit them to version control

---

## Congratulations!

Once you complete all the steps, you'll have a fully functional Coffee Shop application with:
- Role-based authentication using Auth0
- Secure API with JWT validation
- Modern responsive UI with Ionic
- RESTful API design
- Permission-based access control

This demonstrates professional-level authentication and authorization patterns used in real-world applications!

---

**Need Help?**
- Review `CONFIGURATION_STEPS.md` for detailed instructions
- Check `AUTH0_QUICK_REFERENCE.md` for configuration values
- See `START_APP.md` for running the application
- Look for errors in browser console and terminal output
