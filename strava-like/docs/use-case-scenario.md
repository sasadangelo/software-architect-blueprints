# Use Case / Scenario

## 1. Business Context

The platform is a hybrid between a **fitness tracker** and a **social network**, targeting a wide spectrum of users — from casual walkers to competitive cyclists. Its primary value proposition lies not in raw telemetry, but in **community-driven engagement**.

### Strategic Goals:
- Increase **retention** and **daily active usage** through:
  - Social accountability
  - Gamification (badges, challenges, streaks)
  - Peer interaction and recognition
- Drive **monetization** via:
  - **Premium subscriptions**: Advanced analytics (e.g., heart rate zones, live segments, fatigue modeling)
  - **Branded events**: Sponsored challenges or partner leaderboards
  - **In-app commerce**: Gear marketplace with affiliate links (e.g., wearables, shoes, bikes)

### Product Philosophy:
Users should derive value even on rest days — whether through cheering on friends, joining virtual events, or exploring shared goals — creating a **habit-forming platform** beyond workout logging.

---

## 2. Personas & Usage Patterns

| Persona                | Characteristics                                                  | Key Features Used                                            |
| ---------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| **Solo Athletes**      | Focused on personal progress, with occasional social interaction | Workout uploads, segments, performance graphs                |
| **Social Enthusiasts** | Frequent posters and commenters, motivated by interaction        | Feed, comments, kudos, clubs                                 |
| **Club Managers**      | Organize events and build micro-communities                      | Private clubs, event scheduling, moderation                  |
| **Data Nerds**         | Premium-tier subscribers with deep analytics needs               | Heart-rate zones, power curves, GPX exports, VO₂ predictions |

Each persona interacts with the app differently, requiring a **multi-modal architecture** that serves both **real-time social flows** and **data-intensive post-processing**.

---

## 3. Expected Scale

To serve a growing user base while maintaining responsiveness, the platform must scale across multiple axes:

### User & Activity Volume
- **10M+ registered users**
- **2–3M monthly active users (MAUs)**
- **500K+ daily active users (DAUs)**
- **10M+ activity uploads/month**, with weekend spikes
- **500K+ concurrent sessions** during peak events

### Data Footprint
- **Billions of data points/month** from:
  - GPS telemetry
  - Heart rate
  - Elevation gain
  - Cadence / power sensors

### Engagement & Social Graph Load
- **Millions of daily feed queries**
- **Hundreds of thousands of social interactions/day** (kudos, comments, follows)
- **Real-time notifications** for challenges, mentions, and club updates

---

## Architectural Implications

| Dimension                       | Design Implication                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------- |
| **Ingest Throughput**           | Asynchronous pipelines for activity uploads, segment matching, challenge scoring      |
| **Read Optimization**           | Cached feeds, fan-out-on-write for low-latency consumption                            |
| **Burst Handling**              | Elastic autoscaling for weekend surges and event spikes                               |
| **Realtime Delivery**           | WebSockets / push infra for social notifications and live tracking                    |
| **Data Durability & Analytics** | Append-only stores (e.g., S3 + Parquet) feeding into data lakehouse and ML models     |
| **Persona-aware UX**            | Feature flags and service boundaries to deliver tailored experiences per user profile |

