# Coffee Shop Setup Checklist

Use this checklist to track your progress through the setup process.

---

## Phase 1: Auth0 Configuration

### Step 1: Create Auth0 Account
- [ ] Signed up at https://auth0.com
- [ ] Created a tenant
- [ ] Recorded tenant domain: `___________________.us.auth0.com`

### Step 2: Create Application
- [ ] Created Single Page Application named "Coffee Shop"
- [ ] Recorded Client ID: `___________________________________`
- [ ] Added callback URL: `http://localhost:8100`
- [ ] Added callback URL: `http://localhost:8100/tabs/user-page`
- [ ] Added logout URL: `http://localhost:8100`
- [ ] Added web origins: `http://localhost:8100`
- [ ] Clicked "Save Changes"

### Step 3: Create API
- [ ] Created API named "Coffee Shop API"
- [ ] Set identifier to: `coffee`
- [ ] Selected RS256 signing algorithm
- [ ] Added permission: `get:drinks-detail`
- [ ] Added permission: `post:drinks`
- [ ] Added permission: `patch:drinks`
- [ ] Added permission: `delete:drinks`
- [ ] Enabled RBAC in API settings
- [ ] Enabled "Add Permissions in the Access Token"
- [ ] Clicked "Save"

### Step 4: Create Roles
- [ ] Created "Barista" role
- [ ] Added `get:drinks-detail` permission to Barista role
- [ ] Created "Manager" role
- [ ] Added all 4 permissions to Manager role

### Step 5: Create Users
- [ ] Created user: `barista@coffeeshop.com` with password `Test123!`
- [ ] Assigned Barista role to barista user
- [ ] Created user: `manager@coffeeshop.com` with password `Test123!`
- [ ] Assigned Manager role to manager user

---

## Phase 2: Application Configuration

### Step 6: Update Frontend Configuration
- [ ] Opened `src/environments/environment.ts`
- [ ] Replaced `YOUR-TENANT-NAME` with my Auth0 prefix
- [ ] Replaced `YOUR-CLIENT-ID` with my Client ID
- [ ] Verified `audience` is set to `coffee`
- [ ] Saved the file

### Step 7: Update Backend Configuration
- [ ] Opened `src/auth/auth.py`
- [ ] Replaced `YOUR-TENANT-NAME.us.auth0.com` with my full Auth0 domain
- [ ] Verified `API_AUDIENCE` is set to `coffee`
- [ ] Saved the file

### Step 8: Update Token Helper (Optional)
- [ ] Opened `get_token.html`
- [ ] Replaced `YOUR-TENANT-NAME.us.auth0.com` with my full Auth0 domain
- [ ] Replaced `YOUR-CLIENT-ID` with my Client ID
- [ ] Saved the file

---

## Phase 3: Install Dependencies

### Step 9: Backend Dependencies
- [ ] Opened terminal
- [ ] Navigated to project directory
- [ ] Ran: `pip install -r requirements.txt`
- [ ] No errors during installation

### Step 10: Frontend Dependencies
- [ ] Checked Node.js version: `node --version`
- [ ] Noted Node version: `________________`
- [ ] Ran: `npm install` (or with legacy provider if Node 17+)
- [ ] No errors during installation

---

## Phase 4: Run Application

### Step 11: Start Backend
- [ ] Opened Terminal 1
- [ ] Ran: `python run_server.py`
- [ ] Backend started on port 5000
- [ ] No error messages
- [ ] Kept terminal running

### Step 12: Start Frontend
- [ ] Opened Terminal 2
- [ ] Ran: `npm start` (or with legacy provider)
- [ ] Frontend started on port 8100
- [ ] No error messages
- [ ] Kept terminal running

### Step 13: Populate Database (Optional)
- [ ] Ran: `python populate_db.py`
- [ ] Sample drinks added to database

---

## Phase 5: Testing

### Step 14: Test as Barista
- [ ] Opened browser to `http://localhost:8100`
- [ ] Clicked on User tab
- [ ] Clicked "Log In"
- [ ] Logged in as `barista@coffeeshop.com`
- [ ] Redirected back to app successfully
- [ ] Went to Drink Menu tab
- [ ] Can see drinks
- [ ] "Create Drink" button is NOT visible
- [ ] Clicked on a drink to view details
- [ ] Cannot edit or delete drinks

### Step 15: Test as Manager
- [ ] Clicked "Log Out" in User tab
- [ ] Clicked "Log In" again
- [ ] Logged in as `manager@coffeeshop.com`
- [ ] Redirected back to app successfully
- [ ] Went to Drink Menu tab
- [ ] Can see drinks
- [ ] "Create Drink" button IS visible
- [ ] Clicked "Create Drink"
- [ ] Created a new drink successfully
- [ ] Clicked on an existing drink
- [ ] Edited the drink successfully
- [ ] Deleted a drink successfully

---

## Verification Checklist

### Auth0 Verification
- [ ] Domain is correct in all config files
- [ ] Client ID is correct in frontend config
- [ ] API identifier is `coffee` everywhere
- [ ] All callback URLs are configured
- [ ] RBAC is enabled
- [ ] Permissions exist in API
- [ ] Roles exist with correct permissions
- [ ] Users exist with roles assigned

### Application Verification
- [ ] Backend runs without errors
- [ ] Frontend runs without errors
- [ ] No console errors in browser (F12)
- [ ] Can login as Barista
- [ ] Can login as Manager
- [ ] Barista has limited permissions
- [ ] Manager has full permissions
- [ ] JWT token visible in User tab
- [ ] Can create drinks as Manager
- [ ] Can edit drinks as Manager
- [ ] Can delete drinks as Manager

---

## Troubleshooting Record

If you encounter issues, note them here for reference:

### Issue 1:
**Problem**:
**Solution**:

### Issue 2:
**Problem**:
**Solution**:

### Issue 3:
**Problem**:
**Solution**:

---

## Configuration Values (For Your Reference)

Record your Auth0 values here for easy access:

**Auth0 Domain**: `___________________________________`
**Auth0 Tenant Prefix**: `___________________________________`
**Client ID**: `___________________________________`
**API Identifier**: `coffee` (fixed value)

**Test Users**:
- Barista: `barista@coffeeshop.com` / `Test123!`
- Manager: `manager@coffeeshop.com` / `Test123!`

---

## Completion Status

- [ ] All setup steps completed
- [ ] All tests passed
- [ ] Application working as expected
- [ ] Ready to use the Coffee Shop app!

**Setup Completed On**: __________________ (Date)

---

## Notes

Use this space to record any additional notes, customizations, or observations:

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________
