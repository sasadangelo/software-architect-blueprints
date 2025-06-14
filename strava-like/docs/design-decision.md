# Trade-offs & Design Decisions

The platform architecture balances performance, scalability, and developer velocity. Below are key architectural choices, rationales, and associated trade-offs.

---

## 1. Fan-out-on-Write vs. Fan-out-on-Read

### **Decision**
- A **hybrid model** was adopted:
  - **Fan-out-on-write** for the majority of users (pre-computes feed entries).
  - **Fan-out-on-read** for high-fanout users (e.g., influencers with thousands of followers).

### **Rationale**
- Precomputing reduces **read latency** and spreads write load.
- For high-fanout users, write amplification becomes prohibitively expensive.
- The hybrid approach optimizes the 95th percentile use case while preventing fan-out storms.

### **Trade-offs**
- **Operational complexity**:
  - Dual execution paths based on user tier or follower count.
  - Increases testing scope and edge case handling.
- **Code maintainability**:
  - Business logic must be aware of tiering to handle routing correctly.

---

## 2. Polyglot Persistence

### **Decision**
- Core data stores:
  - `PostgreSQL` for relational integrity
  - `Redis` for low-latency caching
  - `Kafka` for async event pipelines
  - `S3` for media and blob storage
- `Neo4j` (graph DB) considered but deferred.

### **Rationale**
- Chosen technologies align with core access patterns and scaling needs.
- Avoiding a dedicated graph DB simplifies ops, hiring, and local development.

### **Trade-offs**
- Certain queries (e.g., “mutual followers in a club”) are less performant without graph traversal.
- Redis caching mitigates this, but introduces:
  - **Cache invalidation complexity**
  - **Stale reads** under heavy churn

---

## 3. Real-Time GPS Sync vs. Post-Workout Upload

### **Decision**
- **Post-workout upload** is the default path.
- **Real-time GPS sync** is opt-in for premium use cases (live tracking, virtual races).

### **Rationale**
- Real-time sync:
  - Increases **backend throughput**, mobile **power usage**, and **network churn**
  - Complicates data consistency and recovery
- Post-upload provides **better battery life**, simpler batching, and offline tolerance.

### **Trade-offs**
- Limits support for:
  - Live cheering
  - Real-time leaderboard updates
  - On-the-fly pacing features
- Real-time streaming will be **progressively enabled** via feature flags in future releases.

---

## 4. Microservices vs. Monolith

### **Decision**
- Adopted **microservices** from early development.
- Logical separation into services:
  - `activity`, `feed`, `user`, `challenge`, `media`, etc.

### **Rationale**
- Services scale independently:
  - `Feed` and `activity ingestion` have divergent latency and throughput profiles.
- Teams can work in parallel with clearer domain ownership.

### **Trade-offs**
- Requires a strong **platform foundation**:
  - Service discovery
  - Tracing
  - CI/CD isolation
  - Fault-tolerant deployment patterns
- **Higher initial complexity**, especially for smaller teams.

---

## 5. Event-Driven vs. Synchronous Workflows

### **Decision**
- **Async workflows** for all non-critical paths:
  - Feed propagation
  - Leaderboard updates
  - Notifications
- **Synchronous (request-response)** only for:
  - Auth
  - Direct user queries

### **Rationale**
- Event-driven architecture improves:
  - **Scalability**
  - **Retry semantics**
  - **Queue prioritization**
- Enables smoother handling of:
  - High ingest variance (e.g., challenge spikes, third-party syncs)

### **Trade-offs**
- Introduces **eventual consistency**
- Requires robust tooling:
  - DLQs (Dead Letter Queues)
  - Idempotent consumers
  - Event replay infrastructure
- Harder to **debug** and **trace flows** without proper observability

---

# Architectural Debt & Mitigations

| Debt Area              | Issue                                | Mitigation Strategy                                |
| ---------------------- | ------------------------------------ | -------------------------------------------------- |
| Legacy feed path       | Some paths assume synchronous writes | Being migrated to Kafka-based fan-out services     |
| Challenge rules        | Logic was hardcoded                  | Replaced with a rule engine for dynamic evaluation |
| Permission enforcement | Scattered across services            | Centralized into a unified Access Policy Service   |

