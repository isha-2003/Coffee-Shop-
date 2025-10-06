# Auth0 Configuration Checklist

## ✅ Required Information from Auth0 Dashboard

After setting up Auth0, you need to collect these values:

### From Applications > Applications > Your SPA App > Settings:
- **Domain**: `your-tenant-name.us.auth0.com`
- **Client ID**: `abc123def456...` (long string)

### From Applications > APIs > Your API > Settings:
- **API Identifier**: `coffee-shop` (what you set as identifier)

## 🔧 Update These Files:

### 1. Update `src/auth/auth.py`:
```python
AUTH0_DOMAIN = 'your-actual-domain.us.auth0.com'
API_AUDIENCE = 'your-actual-api-identifier'
```

### 2. Update `get_token.html`:
```javascript
domain: 'your-actual-domain.us.auth0.com',
clientId: 'your-actual-client-id',
audience: 'your-actual-api-identifier'
```

## 🧪 Testing Steps:

1. **Get JWT Tokens**:
   - Open `get_token.html` in browser
   - Login as `barista@coffeeshop.com` (password: `Test123!`)
   - Copy the JWT token
   - Repeat for `manager@coffeeshop.com`

2. **Test API with Postman**:
   - Import the postman collection
   - Set Authorization header: `Bearer YOUR_JWT_TOKEN`
   - Test endpoints with different user roles

## 🔑 Test Users Created:

| Email | Password | Role | Permissions |
|-------|----------|------|-------------|
| barista@coffeeshop.com | Test123! | Barista | get:drinks-detail |
| manager@coffeeshop.com | Test123! | Manager | All permissions |

## 🚨 Common Issues:

1. **"Invalid audience"**: Check API_AUDIENCE matches your API identifier
2. **"Invalid issuer"**: Check AUTH0_DOMAIN is correct
3. **"Permission denied"**: Check user has correct role assigned
4. **CORS errors**: Make sure callback URLs are set correctly