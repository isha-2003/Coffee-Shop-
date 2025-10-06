# Coffee Shop App - Visual Setup Guide

This guide provides a visual walkthrough of the application setup and functionality.

---

## Setup Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    STEP 1: AUTH0 SETUP                       │
│                                                               │
│  Auth0.com → Create Account → Create Application             │
│     ↓                                                         │
│  Create API → Add Permissions → Enable RBAC                  │
│     ↓                                                         │
│  Create Roles (Barista, Manager)                             │
│     ↓                                                         │
│  Create Users → Assign Roles                                 │
│                                                               │
│  Time: 20-30 minutes                                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                STEP 2: CONFIGURE APPLICATION                 │
│                                                               │
│  Update environment.ts (Frontend)                            │
│    • Auth0 domain prefix                                     │
│    • Client ID                                               │
│    • API audience                                            │
│     ↓                                                         │
│  Update auth.py (Backend)                                    │
│    • Auth0 full domain                                       │
│    • API audience                                            │
│                                                               │
│  Time: 5-10 minutes                                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 3: INSTALL & RUN                           │
│                                                               │
│  pip install -r requirements.txt                             │
│  npm install                                                 │
│     ↓                                                         │
│  Terminal 1: python run_server.py (port 5000)               │
│  Terminal 2: npm start (port 8100)                           │
│                                                               │
│  Time: 5-10 minutes                                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    STEP 4: TEST APP                          │
│                                                               │
│  Open http://localhost:8100                                  │
│     ↓                                                         │
│  Test Barista Login → Verify limited access                 │
│  Test Manager Login → Verify full access                    │
│                                                               │
│  Time: 5-10 minutes                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Application Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                         USER FLOW                               │
└────────────────────────────────────────────────────────────────┘

User Opens App (localhost:8100)
        ↓
User Clicks "Log In"
        ↓
Redirected to Auth0 Login Page
        ↓
Enters Credentials
        ↓
Auth0 Validates & Issues JWT Token
        ↓
User Redirected Back to App with Token
        ↓
App Stores Token Locally
        ↓
App Makes API Call to Backend (port 5000)
        ↓
Backend Validates JWT Token
        ↓
Backend Checks Permissions in Token
        ↓
Backend Returns Data if Authorized
        ↓
Frontend Displays Data Based on User Role
```

---

## Permission Flow

```
┌──────────────────────────────────────────────────────────────┐
│                    PERMISSION SYSTEM                          │
└──────────────────────────────────────────────────────────────┘

                    JWT Token Contains:
                    ┌────────────────┐
                    │  User Identity │
                    │  Permissions   │
                    │  Role Info     │
                    │  Expiration    │
                    └────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ↓                 ↓                  ↓
  get:drinks-detail  post:drinks      patch:drinks
         │                 │                  │
         ↓                 ↓                  ↓
    View Details     Create Drink      Edit Drink


┌─────────────────┐          ┌──────────────────────┐
│  BARISTA ROLE   │          │   MANAGER ROLE       │
├─────────────────┤          ├──────────────────────┤
│ Permissions:    │          │ Permissions:         │
│ ✓ View drinks   │          │ ✓ View drinks        │
│ ✗ Create drinks │          │ ✓ Create drinks      │
│ ✗ Edit drinks   │          │ ✓ Edit drinks        │
│ ✗ Delete drinks │          │ ✓ Delete drinks      │
└─────────────────┘          └──────────────────────┘
```

---

## UI Comparison: Barista vs Manager

```
┌────────────────────────────────────────────────────────────┐
│                    BARISTA VIEW                             │
│                  (Limited Access)                           │
└────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════╗
║      Uda-Spice Latte Cafe              ║
╠════════════════════════════════════════╣
║                                        ║
║  ┌──────────┐  ┌──────────┐           ║
║  │  Latte   │  │ Espresso │           ║
║  │  [Drink  │  │ [Drink   │           ║
║  │   Icon]  │  │  Icon]   │           ║
║  └──────────┘  └──────────┘           ║
║                                        ║
║  NO "Create Drink" button visible      ║
║                                        ║
╠════════════════════════════════════════╣
║  [Drink Menu] [User Page]              ║
╚════════════════════════════════════════╝


┌────────────────────────────────────────────────────────────┐
│                    MANAGER VIEW                             │
│                   (Full Access)                             │
└────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════╗
║      Uda-Spice Latte Cafe              ║
╠════════════════════════════════════════╣
║                                        ║
║  ┌──────────┐  ┌──────────┐  ┌──────┐ ║
║  │  Latte   │  │ Espresso │  │  +   │ ║
║  │  [Drink  │  │ [Drink   │  │Create│ ║
║  │   Icon]  │  │  Icon]   │  │Drink │ ║
║  └──────────┘  └──────────┘  └──────┘ ║
║                                        ║
║  "Create Drink" button IS visible      ║
║  Can click drinks to edit/delete       ║
║                                        ║
╠════════════════════════════════════════╣
║  [Drink Menu] [User Page]              ║
╚════════════════════════════════════════╝
```

---

## API Endpoint Security

```
┌────────────────────────────────────────────────────────────┐
│                  API ENDPOINT MATRIX                        │
└────────────────────────────────────────────────────────────┘

Endpoint              Public  Barista  Manager
─────────────────────────────────────────────
GET /drinks             ✓       ✓        ✓
GET /drinks-detail      ✗       ✓        ✓
POST /drinks            ✗       ✗        ✓
PATCH /drinks/<id>      ✗       ✗        ✓
DELETE /drinks/<id>     ✗       ✗        ✓

Legend:
  ✓ = Access Granted
  ✗ = Access Denied (403 Forbidden)
```

---

## Configuration File Locations

```
project-root/
│
├── Frontend Configuration
│   └── src/environments/environment.ts
│       ┌──────────────────────────────────┐
│       │ auth0: {                         │
│       │   url: 'YOUR-TENANT-PREFIX',     │
│       │   audience: 'coffee',            │
│       │   clientId: 'YOUR-CLIENT-ID'     │
│       │ }                                │
│       └──────────────────────────────────┘
│
├── Backend Configuration
│   └── src/auth/auth.py
│       ┌──────────────────────────────────────────────┐
│       │ AUTH0_DOMAIN = 'YOUR-DOMAIN.us.auth0.com'   │
│       │ API_AUDIENCE = 'coffee'                     │
│       └──────────────────────────────────────────────┘
│
└── Token Helper (Optional)
    └── get_token.html
        ┌──────────────────────────────────────────┐
        │ domain: 'YOUR-DOMAIN.us.auth0.com',     │
        │ clientId: 'YOUR-CLIENT-ID',             │
        │ audience: 'coffee'                      │
        └──────────────────────────────────────────┘
```

---

## Request Flow with Authentication

```
┌──────────────────────────────────────────────────────────┐
│             AUTHENTICATED REQUEST FLOW                    │
└──────────────────────────────────────────────────────────┘

Frontend (localhost:8100)
    │
    │ 1. User clicks "Create Drink"
    │
    ↓
Check: Does user have JWT token?
    │
    ├─ NO → Redirect to Auth0 Login
    │
    └─ YES → Continue
         │
         │ 2. Make API request with JWT token
         │    Header: Authorization: Bearer <JWT>
         │
         ↓
Backend (localhost:5000)
    │
    │ 3. Extract JWT from header
    │
    ↓
Validate JWT Token
    │
    ├─ Invalid → Return 401 Unauthorized
    │
    └─ Valid → Continue
         │
         │ 4. Decode JWT to get permissions
         │
         ↓
Check Permissions
    │
    ├─ Missing 'post:drinks' → Return 403 Forbidden
    │
    └─ Has 'post:drinks' → Continue
         │
         │ 5. Process request
         │
         ↓
Database Operation
    │
    │ 6. Create drink in database
    │
    ↓
Return Success Response
    │
    │ 7. Send drink data back
    │
    ↓
Frontend
    │
    │ 8. Display new drink in UI
    │
    ↓
Done!
```

---

## Auth0 Dashboard Navigation

```
┌─────────────────────────────────────────────────────────┐
│               AUTH0 DASHBOARD MAP                        │
└─────────────────────────────────────────────────────────┘

Auth0 Dashboard (auth0.com)
│
├── Applications
│   └── Applications
│       └── Coffee Shop (SPA)
│           ├── Settings
│           │   ├── Domain ← Copy this
│           │   ├── Client ID ← Copy this
│           │   └── Application URIs ← Configure these
│           └── Connections
│
├── Applications
│   └── APIs
│       └── Coffee Shop API
│           ├── Settings
│           │   ├── Identifier: 'coffee'
│           │   ├── Enable RBAC ← Toggle ON
│           │   └── Add Permissions in Token ← Toggle ON
│           └── Permissions ← Add 4 permissions here
│
└── User Management
    ├── Roles
    │   ├── Barista ← Create & add permissions
    │   └── Manager ← Create & add permissions
    │
    └── Users
        ├── barista@coffeeshop.com ← Create & assign Barista role
        └── manager@coffeeshop.com ← Create & assign Manager role
```

---

## Troubleshooting Decision Tree

```
┌─────────────────────────────────────────┐
│     Application Not Working?             │
└─────────────────────────────────────────┘
                 │
      ┌──────────┴──────────┐
      ↓                     ↓
Can you access         Backend
localhost:8100?        running?
      │                     │
  NO  │  YES            NO  │  YES
      ↓                     ↓
Check npm start      Can you login?
and Node.js              │
version              NO  │  YES
                         ↓
                Check Auth0    Are permissions
                config files   working correctly?
                         │              │
                        YES         NO  │  YES
                         ↓              ↓
                    Check roles   App is working!
                    assigned in   Continue testing
                    Auth0 Dashboard
```

---

## Testing Scenarios

```
┌──────────────────────────────────────────────────────────┐
│                   TEST SCENARIOS                          │
└──────────────────────────────────────────────────────────┘

Scenario 1: Public Access
┌─────────────────────┐
│ No login required   │  → Visit /drinks endpoint
│ Should see drinks   │  → Success: Returns drink list
└─────────────────────┘

Scenario 2: Barista Login
┌─────────────────────┐
│ Login as Barista    │  → See drinks in UI
│ View details only   │  → No Create button
│ Cannot edit/delete  │  → Click drink: View only
└─────────────────────┘

Scenario 3: Manager Login
┌─────────────────────┐
│ Login as Manager    │  → See drinks in UI
│ Full access         │  → Create button visible
│ Can create/edit     │  → Can modify all drinks
└─────────────────────┘

Scenario 4: Invalid Token
┌─────────────────────┐
│ Expired token       │  → API returns 401
│ Modified token      │  → Login redirects
└─────────────────────┘

Scenario 5: Missing Permission
┌─────────────────────┐
│ Barista tries POST  │  → API returns 403
│ Barista tries PATCH │  → Access denied
└─────────────────────┘
```

---

## Success Checklist Visual

```
✓ = Completed    ✗ = Not Yet    ⧗ = In Progress

Setup Progress:
┌─────────────────────────────────────────┐
│ [✓] Auth0 account created                │
│ [✓] Application created                  │
│ [✓] API configured                       │
│ [✓] Permissions added                    │
│ [✓] Roles created                        │
│ [✓] Users created                        │
│ [✓] Config files updated                 │
│ [✓] Dependencies installed               │
│ [✓] Backend running                      │
│ [✓] Frontend running                     │
│ [✓] Barista login works                  │
│ [✓] Manager login works                  │
│ [✓] Permissions verified                 │
└─────────────────────────────────────────┘

When all items are ✓, you're ready to use the app!
```

---

## Configuration Values Template

```
╔════════════════════════════════════════════════════╗
║          YOUR CONFIGURATION VALUES                 ║
╠════════════════════════════════════════════════════╣
║                                                    ║
║  Auth0 Full Domain:                               ║
║  ┌──────────────────────────────────────────┐    ║
║  │ ___________________.us.auth0.com         │    ║
║  └──────────────────────────────────────────┘    ║
║                                                    ║
║  Auth0 Tenant Prefix (for environment.ts):        ║
║  ┌──────────────────────────────────────────┐    ║
║  │ ___________________                      │    ║
║  └──────────────────────────────────────────┘    ║
║                                                    ║
║  Client ID:                                       ║
║  ┌──────────────────────────────────────────┐    ║
║  │ ___________________________________      │    ║
║  └──────────────────────────────────────────┘    ║
║                                                    ║
║  API Identifier (fixed):                          ║
║  ┌──────────────────────────────────────────┐    ║
║  │ coffee                                   │    ║
║  └──────────────────────────────────────────┘    ║
║                                                    ║
╚════════════════════════════════════════════════════╝

Print this page and fill in your values!
```

---

## Resources & Documentation Links

```
┌──────────────────────────────────────────────────┐
│              HELPFUL RESOURCES                    │
├──────────────────────────────────────────────────┤
│                                                  │
│  Project Documentation:                          │
│  • README.md                                     │
│  • CONFIGURATION_STEPS.md                        │
│  • AUTH0_QUICK_REFERENCE.md                      │
│  • START_APP.md                                  │
│  • SETUP_CHECKLIST.md                            │
│                                                  │
│  External Resources:                             │
│  • Auth0: https://auth0.com/docs                 │
│  • Flask: https://flask.palletsprojects.com/     │
│  • Ionic: https://ionicframework.com/docs        │
│  • Angular: https://angular.io/docs              │
│                                                  │
│  Reference:                                      │
│  • Udacity Video: youtube.com/watch?v=...        │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

This visual guide provides a graphical overview of the Coffee Shop application setup and functionality. For detailed instructions, refer to the documentation files listed in the README.
