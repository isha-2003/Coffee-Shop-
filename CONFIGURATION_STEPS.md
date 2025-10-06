# Coffee Shop App - Complete Configuration Guide

This guide will walk you through setting up the Coffee Shop application exactly as shown in the Udacity reference video.

## Overview

This application demonstrates Role-Based Access Control (RBAC) using Auth0. There are two user roles:
- **Barista**: Can view drink details
- **Manager**: Can view, create, edit, and delete drinks

---

## Part 1: Auth0 Setup

### Step 1: Create Auth0 Account

1. Go to https://auth0.com and sign up for a free account
2. Create a new tenant when prompted
3. Your Auth0 domain will be something like: `dev-abc123.us.auth0.com`
4. Remember your tenant prefix (e.g., `dev-abc123`)

### Step 2: Create a Single Page Application

1. In Auth0 Dashboard, navigate to **Applications** > **Applications**
2. Click **Create Application**
3. Enter application name: `Coffee Shop`
4. Select **Single Page Web Applications**
5. Click **Create**
6. Go to the **Settings** tab
7. Note down the following (you'll need these later):
   - **Domain**: `dev-abc123.us.auth0.com`
   - **Client ID**: A long string like `abc123def456...`
8. Scroll down to **Application URIs** section and configure:
   - **Allowed Callback URLs**:
     ```
     http://localhost:8100, http://localhost:8100/tabs/user-page
     ```
   - **Allowed Logout URLs**:
     ```
     http://localhost:8100
     ```
   - **Allowed Web Origins**:
     ```
     http://localhost:8100
     ```
   - **Allowed Origins (CORS)**:
     ```
     http://localhost:8100
     ```
9. Click **Save Changes** at the bottom

### Step 3: Create an API

1. Navigate to **Applications** > **APIs**
2. Click **Create API**
3. Fill in the details:
   - **Name**: `Coffee Shop API`
   - **Identifier**: `coffee` (IMPORTANT: use exactly this)
   - **Signing Algorithm**: `RS256`
4. Click **Create**
5. Go to the **Permissions** tab
6. Add the following permissions one by one:
   - `get:drinks-detail` - Description: "View drink details"
   - `post:drinks` - Description: "Create drinks"
   - `patch:drinks` - Description: "Update drinks"
   - `delete:drinks` - Description: "Delete drinks"
7. Go to **Settings** tab
8. Scroll down and toggle ON:
   - **Enable RBAC**
   - **Add Permissions in the Access Token**
9. Click **Save**

### Step 4: Create Roles

1. Navigate to **User Management** > **Roles**
2. Click **Create Role**

#### Create Barista Role:
1. Name: `Barista`
2. Description: `Can view drink details`
3. Click **Create**
4. Go to **Permissions** tab
5. Click **Add Permissions**
6. Select `Coffee Shop API`
7. Check the box for: `get:drinks-detail`
8. Click **Add Permissions**

#### Create Manager Role:
1. Click **Create Role** again
2. Name: `Manager`
3. Description: `Full access to manage drinks`
4. Click **Create**
5. Go to **Permissions** tab
6. Click **Add Permissions**
7. Select `Coffee Shop API`
8. Check ALL four permissions:
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
9. Click **Add Permissions**

### Step 5: Create Test Users

1. Navigate to **User Management** > **Users**
2. Click **Create User**

#### Create Barista User:
1. Email: `barista@coffeeshop.com`
2. Password: `Test123!`
3. Connection: `Username-Password-Authentication`
4. Click **Create**
5. After creation, go to the **Roles** tab
6. Click **Assign Roles**
7. Select `Barista`
8. Click **Assign**

#### Create Manager User:
1. Click **Create User** again
2. Email: `manager@coffeeshop.com`
3. Password: `Test123!`
4. Connection: `Username-Password-Authentication`
5. Click **Create**
6. After creation, go to the **Roles** tab
7. Click **Assign Roles**
8. Select `Manager`
9. Click **Assign**

---

## Part 2: Configure Your Application

### Step 6: Update Frontend Configuration

Open `src/environments/environment.ts` and replace the placeholder values:

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'YOUR-TENANT-PREFIX',        // e.g., 'dev-abc123' (WITHOUT .us.auth0.com)
    audience: 'coffee',                // Leave as 'coffee'
    clientId: 'YOUR-CLIENT-ID',        // Paste your Client ID from Step 2
    callbackURL: 'http://localhost:8100',
  }
};
```

**Example:**
```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'dev-abc123',
    audience: 'coffee',
    clientId: 'xYz123AbC456DeF789',
    callbackURL: 'http://localhost:8100',
  }
};
```

### Step 7: Update Backend Configuration

Open `src/auth/auth.py` and update the Auth0 configuration:

```python
AUTH0_DOMAIN = 'YOUR-FULL-DOMAIN.us.auth0.com'  # e.g., 'dev-abc123.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'  # Leave as 'coffee'
```

**Example:**
```python
AUTH0_DOMAIN = 'dev-abc123.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'
```

### Step 8: Update Token Helper Page (Optional)

If you want to use the `get_token.html` file to get JWT tokens for testing:

Open `get_token.html` and update:

```javascript
const auth0 = new auth0.Auth0Client({
    domain: 'YOUR-FULL-DOMAIN.us.auth0.com',  // e.g., 'dev-abc123.us.auth0.com'
    clientId: 'YOUR-CLIENT-ID',               // Paste your Client ID
    authorizationParams: {
        redirect_uri: window.location.origin,
        audience: 'coffee'
    }
});
```

---

## Part 3: Run the Application

### Step 9: Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### Step 10: Start the Backend Server

```bash
python run_server.py
```

The Flask API will run on `http://127.0.0.1:5000`

### Step 11: Install Frontend Dependencies

**Important Note on Node.js Version:**
This project uses Angular 7, which requires Node.js version 12-16. If you're using Node.js 17 or higher, you may encounter build errors.

**Recommended approach:**
1. Install Node Version Manager (nvm)
2. Use Node.js 14 or 16:
   ```bash
   nvm install 14
   nvm use 14
   ```

Then install dependencies:

```bash
npm install
```

**Alternative:** If you must use a newer Node.js version, you can use the legacy OpenSSL provider:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm install
```

### Step 12: Start the Frontend Application

If you're using Node.js 17+ with the legacy provider workaround:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
npm start
```

Or use the standard command if you're on Node.js 14-16:

```bash
npm start
```

or

```bash
ionic serve
```

The Ionic app will run on `http://localhost:8100`

---

## Part 4: Testing the Application

### Step 13: Test as Barista

1. Open your browser and go to `http://localhost:8100`
2. Click on the **User** tab at the bottom
3. Click **Log In**
4. Enter:
   - Email: `barista@coffeeshop.com`
   - Password: `Test123!`
5. You should be redirected back to the app
6. Go to the **Drink Menu** tab
7. You should see the drinks but NO "Create Drink" button (baristas can only view)
8. Click on a drink to view details (but you cannot edit or delete)

### Step 14: Test as Manager

1. In the **User** tab, click **Log Out**
2. Click **Log In** again
3. Enter:
   - Email: `manager@coffeeshop.com`
   - Password: `Test123!`
4. Go to the **Drink Menu** tab
5. You should see the "Create Drink" button (managers have full access)
6. Click **Create Drink** to add a new drink
7. Click on any drink to edit or delete it

---

## Part 5: Populate Sample Drinks (Optional)

To add sample drinks to the database:

```bash
python populate_db.py
```

This will add some starter drinks like Latte, Cappuccino, etc.

---

## Troubleshooting

### Common Issues:

1. **"Invalid audience" error**:
   - Make sure `API_AUDIENCE` in `auth.py` matches your API identifier exactly
   - Make sure `audience` in `environment.ts` matches your API identifier

2. **"Invalid issuer" error**:
   - Check that `AUTH0_DOMAIN` in `auth.py` is correct
   - Make sure it includes `.us.auth0.com` or your region's domain

3. **"Permission denied" error**:
   - Verify the user has the correct role assigned in Auth0
   - Make sure RBAC is enabled in your API settings
   - Ensure "Add Permissions in the Access Token" is enabled

4. **CORS errors**:
   - Verify callback URLs in Auth0 match exactly
   - Check that CORS is enabled in the Flask app

5. **Login redirects to wrong page**:
   - Verify callback URLs in Auth0 Application settings
   - Check `callbackURL` in `environment.ts`

6. **Permissions not in JWT token**:
   - Go to API Settings in Auth0
   - Enable "Add Permissions in the Access Token"
   - Enable "Enable RBAC"

---

## Summary of Required Values

Make sure you have these three values from Auth0:

| Configuration | Where to Find | Example | Where to Use |
|--------------|---------------|---------|--------------|
| **Domain** | Applications > Your SPA > Settings | `dev-abc123.us.auth0.com` | `auth.py` (full domain), `environment.ts` (prefix only) |
| **Client ID** | Applications > Your SPA > Settings | `xYz123AbC456DeF789` | `environment.ts` |
| **API Identifier** | Applications > APIs > Your API | `coffee` | Already set correctly |

---

## Next Steps

Once everything is configured and running:

1. Test both user roles to see the difference in permissions
2. Try creating, editing, and deleting drinks as a manager
3. Try viewing drinks as a barista
4. Explore the JWT tokens in the User page to understand how permissions work

Congratulations! Your Coffee Shop application is now fully configured and should look exactly like the Udacity reference video.
