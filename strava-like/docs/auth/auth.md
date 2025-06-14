# AuthService — Use Cases & Sequence Diagrams

## 1. Registration

### Proprietary Registration (Email + Password)

Users register by providing email and password. After registration, an **email validation** step is required before the account is fully active.

- User submits registration data.
- AuthService creates the user with default role `MEMBER` (or specified role).
- Sends validation email with a unique token.
- User clicks validation link to activate the account.

---

### Sequence Diagram — Proprietary Registration & Email Validation

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant AuthService
    participant UserService
    participant EmailService

    User->>Frontend: Submit registration (first name, last name, email, password)
    Frontend->>AuthService: Create user request
    AuthService->>UserService: Create user with MEMBER role, inactive status
    UserService-->>AuthService: Confirmation
    AuthService->>EmailService: Send email validation with token
    AuthService-->>Frontend: Registration OK, waiting for email validation
    User->>AuthService: Click validation link with token
    AuthService->>UserService: Validate token and activate user
    UserService-->>AuthService: User activated
    AuthService-->>User: Email validated confirmation
```

### OAuth Registration (Google, Facebook)

Users can also register using OAuth providers. OAuth registration combines user creation with OAuth login.

* User authenticates with OAuth provider.
* AuthService fetches user info from OAuth provider.
* If user exists, logs in; else creates user and marks email as validated.
* Assigns default role MEMBER.

#### Sequence Diagram — OAuth Registration

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant OAuthProvider
    participant AuthService
    participant UserService

    User->>Frontend: Click OAuth register/login
    Frontend->>OAuthProvider: Redirect for authentication
    OAuthProvider-->>Frontend: Authorization code
    Frontend->>AuthService: Exchange code for token + user info
    AuthService->>UserService: Lookup user by OAuth ID or email
    alt User exists
        UserService-->>AuthService: User info with roles
    else New user
        AuthService->>UserService: Create user with MEMBER role, email validated
        UserService-->>AuthService: Confirmation of creation
    end
    AuthService-->>Frontend: Return JWT with role info
    Frontend-->>User: Access granted
```

## 2. Login

Users can log in either via:

* Proprietary method (email + password)
* OAuth (Google, Facebook)

In both cases, the system returns a JWT including user roles.

### Sequence Diagram — Proprietary Login

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant AuthService
    participant UserService

    User->>Frontend: Submit login (email, password)
    Frontend->>AuthService: Authenticate user
    AuthService->>UserService: Verify credentials and check email validated
    UserService-->>AuthService: User info with roles
    AuthService-->>Frontend: Return JWT token
    Frontend-->>User: Login success
```

### Sequence Diagram — OAuth Login

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant OAuthProvider
    participant AuthService
    participant UserService

    User->>Frontend: Click OAuth login
    Frontend->>OAuthProvider: Redirect for auth
    OAuthProvider-->>Frontend: Authorization code
    Frontend->>AuthService: Exchange code for token + user info
    AuthService->>UserService: Lookup user
    UserService-->>AuthService: User with roles
    AuthService-->>Frontend: Return JWT with roles
    Frontend-->>User: Access granted
```

## 3. Role Assignment & Management

Roles Description

* **ROOT**: Super admin, reserved, never used in ordinary operations
* **ADMIN**: Platform administration
* **DEVOPS**: Infrastructure and deployment management
* **MODERATOR**: Content moderation within community features
* **MEMBER**: Default user role
* **PREMIUM_MEMBER**: Paid subscriber with additional features
* **COACH**: A member (normal or premium) who can view private accounts of their trainees

### Role Assignment Flow

* Roles are assigned during user creation or updated by admins.
* Role changes trigger JWT refresh or token revocation.
* Access control enforced at service level via JWT claims and RBAC.

### Example Role Assignment Sequence

```mermaid
sequenceDiagram
    participant Admin
    participant AdminPortal
    participant AuthService
    participant UserService

    Admin->>AdminPortal: Request to change user role
    AdminPortal->>AuthService: Update user role request
    AuthService->>UserService: Persist role change
    UserService-->>AuthService: Confirmation
    AuthService-->>AdminPortal: Role updated
    AdminPortal-->>Admin: Success message
```

## Summary

This documentation covers:

* Proprietary registration with email validation
* OAuth registration and login
* Role definitions and assignment flows

If you want, I can prepare code examples and more detailed sequence diagrams for flows such as password reset, token refresh, or role revocation next.
