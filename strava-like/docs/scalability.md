# Scalability Considerations

This document outlines the core strategies and technical choices made to ensure platform scalability across services, data layers, and integrations.

---

## 1. Application Layer Scaling

### Stateless Services
All core services (e.g., Activity, Feed, Challenge) are designed to be stateless and horizontally scalable. Instances are disposable, fronted by a load balancer, and follow shared-nothing principles to avoid reliance on local state.

### Auto-Scaling
Horizontal Pod Autoscaling (HPA) in Kubernetes is used to scale services based on metrics such as:
- CPU usage
- Memory consumption
- Queue depth

Latency-sensitive services (e.g., Feed, Notification) can leverage custom metrics — such as **event lag** — for faster response and aggressive scale-outs.

### API Gateway Throttling
Rate-limiting is enforced at the API gateway using:
- Client- and IP-based limits
- Redis-backed sliding window or leaky bucket algorithms for burst tolerance

---

## 2. Data Layer Scaling

### Read Optimization
Frequently accessed data — such as recent activity logs or leaderboard snapshots — is cached in Redis using:
- Time-to-live (TTL)
- Least Recently Used (LRU) eviction policies

PostgreSQL read replicas are scaled independently to handle analytic and frontend workloads.

### Sharding Strategies
- **Activity Data:** Sharded by `user_id` across logical partitions (e.g., `Activity_01`, `Activity_02`, ...)
- **Feed Items:** Partitioned by both `actor_id` and `recipient_id`, with composite indexes for fast fan-out and lookup
- **GeoStore:** Uses S3 key prefixing based on region and timestamp for efficient object listing and tiered storage optimization

---

## 3. Feed and Social Graph Fan-out

Feed generation represents a significant scalability challenge. A hybrid fan-out approach is adopted:

### Fan-out on Write (Primary)
When a user posts an activity, the Feed Service immediately pushes precomputed feed rows into follower timelines.

### Fan-out on Read (Fallback)
For high-fanout users (e.g., celebrities), feed content is generated dynamically at read time using paginated queries on Kafka-backed logs or feed index tables.

### Feed Storage
Feeds are stored using:
- Write-optimized column-family stores (e.g., ScyllaDB, Cassandra-like systems)
- Time-to-live (TTL) for ephemeral feed events
- Pre-rendered JSON blobs for fast hydration

---

## 4. Challenge and Leaderboard Processing

### Batch Computation
Leaderboards are processed in batches via stream processing engines such as Apache Flink or Spark Streaming. Challenge validations and segment matching run asynchronously and are decoupled from the main activity ingestion path via Kafka topics.

### Windowed Aggregation
To avoid full-history scans, challenge statistics are windowed into time intervals (daily, weekly, etc.) and stored as materialized views indexed by challenge and segment IDs.

---

## 5. Geo and Sensor Data Ingestion

### High-Frequency Ingest
Sensor and GPS data is ingested in high-volume batches to:
- Reduce memory pressure via checkpointing
- Avoid write amplification on time-series databases
- Optimize throughput during ingestion spikes

### Compression
GPS points are delta-encoded and gzipped before being persisted. Rehydration is deferred to visualization or export phases — not performed during real-time interactions.

---

## 6. Third-Party Traffic Bursts

### Ingestion Resilience
Traffic spikes from external services (e.g., Garmin, Apple Health) are handled through:
- Decoupled ingestion queues
- Throttled ETL pipelines
- Circuit breakers and retry policies for each integration

These safeguards help absorb bursts, prevent upstream overloads, and mitigate the risk of fan-out storms.

---
