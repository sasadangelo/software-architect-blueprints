# Security Architecture

This section outlines the security model of the platform, including authentication, data protection, IAM, and secure development practices.

---

## 1. Authentication & Authorization

### **Authentication**
- All client interactions use **OAuth 2.0 with PKCE** for mobile authentication flows.
- **JWTs** are issued and signed by the **Auth Service**, containing the user ID, scopes, and expiration time.
- **Refresh tokens** are rotated and **encrypted at rest**.

### **Federated Login**
- Supports **Google, Apple, and Facebook** logins, always linked to a native user identity.
- Social login tokens are **validated server-side** and are **never trusted directly** by clients.

### **Authorization**
- Every service **validates the JWT** and enforces **scope-based rules** (e.g., `read:feed`, `post:activity`).
- **RBAC (Role-Based Access Control)** governs access to internal tools (e.g., admin, moderator dashboards).

---

## 2. Data Protection

### **At Rest**
- **PostgreSQL, Redis, and object stores** are encrypted with **AES-256** using **customer-managed keys (CMKs)**.
- **Sensitive fields** (e.g., email, health metrics) are encrypted at the **application layer** before DB insertion.

### **In Transit**
- All traffic is secured via **TLS 1.2+** (client-to-server and inter-service).
- **Mutual TLS (mTLS)** is enforced for **gRPC** communication between backend services.

### **Field-Level Masking**
- **Sensitive fields** are masked or redacted in logs and dashboards.
- Observability tooling performs **field tagging** and **automated PII scanning** before ingestion.

### **Geo Privacy**
- Activities marked as **private** or **followers-only** are fully excluded from feeds, leaderboards, and search.
- **Heatmap data** is anonymized and derived only from **public activities**, with **geo-blurring** near home zones.

---

## 3. IAM Design & Secrets Management

### **Secrets Management**
- **API keys, DB credentials, and webhook tokens** are stored in a **centralized vault** (e.g., HashiCorp Vault, AWS Secrets Manager).
- Secrets are **injected at runtime** via environment variables.
- **Automated rotation policies** are applied to short-lived credentials.

### **IAM Design**
- Each microservice has a **unique identity** and a **minimal set of roles**.
- IAM policies are scoped to **least privilege** (e.g., read-only S3, write-only Kafka).
- **CI/CD agents** assume **temporary roles** using **OIDC trust**.

---

## 4. Secure Coding & API Protection

### **Input Validation**
- All external input is validated via **OpenAPI** or **JSON Schema**.
- Length, format, and boundary checks are enforced both **frontend and backend**.

### **Rate Limiting**
- Per-user and per-IP **rate limits** enforced via **Redis** or **API Gateway** plugins.
- **Abuse detection models** (e.g., login storms, spam) inform **dynamic throttling policies**.

### **Replay Protection**
- All signed requests include **nonces** or **timestamps**.
- Webhooks and activity uploads use **HMAC signatures** to **validate origin** and prevent tampering.

### **Code Security**
- **Static analysis (SAST)** and **dependency scanning** are part of the CI pipeline.
- **Secrets detection** (e.g., GitLeaks) blocks accidental leaks at commit time.
- All critical code paths undergo **peer review** and **audited pull requests**.

---
