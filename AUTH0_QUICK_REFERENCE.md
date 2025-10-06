# Auth0 Configuration Quick Reference

Use this guide to quickly fill in your Auth0 configuration values.

---

## Configuration Checklist

### From Auth0 Dashboard

#### 1. Auth0 Domain
- **Where to find**: Applications > Applications > Coffee Shop > Settings
- **Look for**: Domain field
- **Example**: `dev-abc123.us.auth0.com`

#### 2. Client ID
- **Where to find**: Applications > Applications > Coffee Shop > Settings
- **Look for**: Client ID field
- **Example**: `xYz123AbC456DeF789GhI012`

#### 3. API Identifier
- **Where to find**: Applications > APIs > Coffee Shop API > Settings
- **Look for**: Identifier field
- **Should be**: `coffee` (as configured in setup)

---

## Files to Update

### File 1: `src/environments/environment.ts`

```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'YOUR-TENANT-PREFIX',        // Just the prefix: 'dev-abc123'
    audience: 'coffee',                // Leave as is
    clientId: 'YOUR-CLIENT-ID',        // Paste your Client ID
    callbackURL: 'http://localhost:8100',
  }
};
```

**Replace:**
- `YOUR-TENANT-PREFIX` with your domain prefix (e.g., `dev-abc123`)
  - **Important**: Use ONLY the prefix, NOT the full domain
- `YOUR-CLIENT-ID` with your actual Client ID

---

### File 2: `src/auth/auth.py`

```python
AUTH0_DOMAIN = 'YOUR-FULL-DOMAIN.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'
```

**Replace:**
- `YOUR-FULL-DOMAIN.us.auth0.com` with your complete Auth0 domain (e.g., `dev-abc123.us.auth0.com`)
  - **Important**: Use the FULL domain including `.us.auth0.com`

---

### File 3: `get_token.html` (Optional - for testing)

```javascript
const auth0 = new auth0.Auth0Client({
    domain: 'YOUR-FULL-DOMAIN.us.auth0.com',
    clientId: 'YOUR-CLIENT-ID',
    authorizationParams: {
        redirect_uri: window.location.origin,
        audience: 'coffee'
    }
});
```

**Replace:**
- `YOUR-FULL-DOMAIN.us.auth0.com` with your complete Auth0 domain
- `YOUR-CLIENT-ID` with your actual Client ID

---

## Example Configuration

Let's say your Auth0 gives you:
- **Domain**: `dev-abc123.us.auth0.com`
- **Client ID**: `xYz123AbC456DeF789`

### Then your files should look like:

#### `src/environments/environment.ts`
```typescript
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'dev-abc123',                    // ← Just the prefix
    audience: 'coffee',
    clientId: 'xYz123AbC456DeF789',       // ← Your Client ID
    callbackURL: 'http://localhost:8100',
  }
};
```

#### `src/auth/auth.py`
```python
AUTH0_DOMAIN = 'dev-abc123.us.auth0.com'  # ← Full domain
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'
```

#### `get_token.html`
```javascript
const auth0 = new auth0.Auth0Client({
    domain: 'dev-abc123.us.auth0.com',    // ← Full domain
    clientId: 'xYz123AbC456DeF789',       // ← Your Client ID
    authorizationParams: {
        redirect_uri: window.location.origin,
        audience: 'coffee'
    }
});
```

---

## Common Mistakes to Avoid

1. **Using full domain in environment.ts**: Use ONLY the prefix (e.g., `dev-abc123`), not `dev-abc123.us.auth0.com`

2. **Using prefix in auth.py**: Use the FULL domain (e.g., `dev-abc123.us.auth0.com`), not just `dev-abc123`

3. **Wrong API identifier**: Must be `coffee` in all three places

4. **Forgetting to save in Auth0**: Always click "Save Changes" in Auth0 Dashboard after configuration

---

## Verification

Before running the app, verify:

- [ ] Domain is correct in both frontend and backend
- [ ] Client ID is correct in frontend
- [ ] API identifier is `coffee` everywhere
- [ ] Callback URLs are configured in Auth0
- [ ] RBAC is enabled in Auth0 API settings
- [ ] Permissions are added to the API
- [ ] Roles are created with correct permissions
- [ ] Test users are created with roles assigned

---

## Test Credentials

After setup, use these credentials:

| Role | Email | Password | Permissions |
|------|-------|----------|-------------|
| **Barista** | barista@coffeeshop.com | Test123! | View drinks only |
| **Manager** | manager@coffeeshop.com | Test123! | Full access |

---

## Need Help?

If you encounter issues:

1. Double-check all three files have correct values
2. Verify Auth0 Dashboard settings match this guide
3. Check browser console for error messages
4. Ensure Flask backend is running on port 5000
5. Ensure frontend is running on port 8100
6. Review the CONFIGURATION_STEPS.md for detailed troubleshooting
