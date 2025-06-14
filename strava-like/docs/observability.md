# Monitoring & Observability

The platform incorporates comprehensive observability practices across logs, metrics, traces, and alerting to ensure reliability, debuggability, and operational insight.

---

## 1. Logging

### **Structured Logging**
- All services emit logs in **JSON format** with consistent fields:
  - `request_id`, `user_id`, `activity_id`, `duration_ms`, etc.
- Logs are streamed via:
  - `Fluent Bit` or `Filebeat`
  - Centralized sinks like `Elasticsearch` or `Loki`

### **Correlation IDs**
- Every request generates a **unique correlation ID** that:
  - Propagates across service boundaries (via headers and log context)
  - Enables full traceability: **mobile app → backend services → DB**

### **Log Hygiene**
- **PII masking rules** enforced at the log pipeline:
  - Secrets, access tokens, raw telemetry, and GPS coordinates are redacted
  - Logs are sanitized before persistence to prevent data leaks

---

## 2. Metrics

### **System Metrics**
- Exported via **Prometheus** node/pod exporters:
  - CPU, memory, disk, network
  - Alerting on:
    - Saturation
    - Resource pressure
    - Pod churn or crash loops

### **Business Metrics**
- Examples include:
  - Activities per minute
  - Feed events per second
  - Challenge joins, leaderboard writes
  - Latency per endpoint, P99 error rate

### **Custom Instrumentation**
- Services expose:
  - **Counters**, **histograms**, and **gauges** using Prometheus client libraries
- Use cases:
  - `badge_evaluations_processed`
  - `gps_points_uploaded`
  - `segment_matches_executed`

---

## 3. Distributed Tracing

### **Tracing System**
- Instrumentation via **OpenTelemetry**
- Covers:
  - HTTP/gRPC calls
  - DB queries
  - Kafka/queue processing
- Exported to:
  - `Jaeger`, `Honeycomb`, or `Tempo`

### **Trace Sampling**
- **Head-based sampling** with adjustable rates:
  - High-priority operations (e.g., activity ingestion) always traced
  - Low-priority jobs (e.g., metrics export) sampled probabilistically

### **Trace Linking**
- All traces are tied to:
  - `user_id`, `request_id`, `session_id`
- Enables debugging of:
  - Latency bottlenecks in feed generation
  - Leaderboard inconsistency
  - Slow async pipeline stages

---

## 4. Alerting & Dashboards

### **Alert Management**
- Alert pipelines use:
  - `Prometheus Alertmanager`, `Opsgenie`, or `PagerDuty`
- Features:
  - Deduplication
  - Escalation paths
  - Silence windows
  - On-call rotations
- Notifications via:
  - Slack, Microsoft Teams, SMS, Email

### **Dashboards**
- Built in **Grafana** per service with:
  - Drill-down into latency, throughput, error rates, etc.
  - Backlog and saturation for queues, DBs, APIs
  - **Business KPIs** for non-technical stakeholders:
    - Active users
    - Challenge completion rates
    - Session length distributions

### **SLOs & Error Budgets**
- Formal SLOs defined for:
  - Activity submission
  - Feed rendering
  - Challenge participation
- Burn rates inform:
  - Rollout pacing
  - Feature flag gating
  - Alert urgency levels

---

## 5. Health Checks & Readiness Probes

### **Liveness & Readiness**
- All services expose:
  - `/healthz` or `/livez` endpoints for Kubernetes integration
  - Liveness: thread pool saturation, memory usage
  - Readiness: DB reachability, queue lag

### **Deep Synthetic Checks**
- Periodic background jobs simulate **real user flows**:
  - Activity insert + feed fetch
  - Join challenge + score update
- Ensures not just system availability, but **business logic correctness**
