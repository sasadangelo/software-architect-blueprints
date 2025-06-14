# Extensibility & Maintainability

This section outlines how the system is designed for long-term flexibility, fast iteration, and safe collaboration at scale.

---

## 1. Modular Service Boundaries

- Each major domain — **Users**, **Activities**, **Feed**, **Notifications**, **Challenges** — is implemented as its own **independent service**, with its own **schema**, **API**, and **deployable runtime**.
- Services communicate either **asynchronously** via **message queues** or **synchronously** via **gRPC/REST**, depending on latency requirements.

> This **clear separation** allows for:
> - **Independent scaling and deployments**
> - **Faster onboarding** of new engineers
> - Updates to one domain (e.g., leaderboard format, notification triggers) without impacting others (e.g., user profiles, activity ingestion)

---

## 2. Plugin-Oriented Patterns

### **Event Listeners**
- New features (e.g., **achievements**, **live coaching alerts**, **device-based badges**) are added by **subscribing to core events** such as `activity.created` or `challenge.completed`.
- Enables **feature innovation** without touching upstream services.

### **Feature Flags**
- All user-facing features are gated by **dynamic flags** (e.g., **LaunchDarkly**, internal toggles).
- Supports **canary releases**, **A/B testing**, and **targeted rollouts** (e.g., by region, user tier, platform).

### **Custom Challenge Logic**
- The challenge engine is **extensible** via **rule engines** or **embedded scripting** (e.g., **Lua**, **CEL**).
- Enables marketing or community managers to define **new challenge types** (e.g., “climb 2K meters in 3 days”) without backend code changes.

---

## 3. Clean Code & Patterns

### **Domain-Driven Design (DDD)**
- Services are organized by **bounded context** (e.g., **segment scoring**, **follower management**), not by tech stack layer.
- Reduces **code duplication** and **cross-cutting concerns**.

### **Testing & Linting**
- CI enforces:
  - **Linting**
  - **Test coverage thresholds**
  - **Contract tests** for public APIs
- Local development uses **containerized environments** with **seeded databases** and **mock queues** for fast iteration.

### **Monorepo vs Polyrepo**
- **Backend** uses a **polyrepo** approach (one repo per service).
- **Mobile app** may use a **monorepo** with **modular packages**.
- Shared contracts (e.g., **Protobufs**, **GraphQL schemas**) are stored in a **dedicated contract repo**.

---

## 4. Service Versioning & Backward Compatibility

### **API Versioning**
- All public APIs are **versioned** (e.g., `/v1/activities`).
- **Deprecated endpoints** are maintained for a **grace period**, with **observability hooks** to monitor usage.

### **Schema Evolution**
- **PostgreSQL** schemas evolve through **additive migrations** (e.g., adding columns, not removing them).
- **No renaming** of enums or constraints unless **dual-read/write** logic is used.
- For **NoSQL**, each object includes a **schema version** tag for **safe deserialization**.

### **Protocol Compatibility**
- **gRPC** and **Protobuf** contracts:
  - Never remove fields
  - Never reuse field IDs
- **GraphQL**:
  - Deprecated fields are retained with **warning headers**
  - Frontend is linted against deprecated usage

---
