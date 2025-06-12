# 🧭 Use Case & Scenario

This document outlines the strategic use case, target personas, and scale expectations behind the Strava-like fitness application. It helps guide architectural decisions by grounding them in real-world business context and usage patterns.

---

## 1. Business Context

The fitness app targets a broad range of users — from casual walkers to competitive cyclists — but places a strong emphasis on **community engagement** rather than just solo performance tracking. It aims to combine the value of a personal coach with the dynamics of a social network.

### Key Goals:

- Increase user retention through gamification and social accountability
- Encourage recurring engagement, even on non-training days
- Drive monetization through premium features and partnerships

### Monetization Opportunities:

- **Premium Subscriptions**  
  Unlock advanced analytics, live segment tracking, in-depth performance insights, and exclusive challenges.

- **Branded Challenges**  
  Sponsored events and competitions (e.g., “Nike Ride 100km in a week”).

- **In-App Gear Promotion**  
  Integration with marketplaces to promote shoes, bikes, wearables, and accessories (e.g., affiliate model).

---

## 2. Personas & Usage Patterns

Understanding the user base is essential for designing the system’s workflows and data models.

| Persona | Description | Key Behaviors |
|--------|-------------|----------------|
| 🏃‍♂️ **Solo Athletes** | Users who train independently and track progress over time. | Log workouts, view historical trends, join occasional challenges. |
| 👥 **Social Enthusiasts** | Community-focused users who enjoy sharing, commenting, and engaging. | Frequent social interactions, content posting, feed scrolling. |
| 📅 **Club Managers** | Organizers who manage group rides or runs. | Create private challenges, moderate club feeds, manage leaderboards. |
| 📊 **Data Nerds** | Power users with deep interest in analytics. | Explore heart-rate zones, recovery stats, training load, export data. |

---

## 3. Expected Scale

To support a growing and engaged user base, the platform must be designed with the following scale expectations in mind:

### Users

- **10M+ registered users**
- **2–3M Monthly Active Users (MAUs)**
- **~500K Daily Active Users (DAUs)**

### Activity Data

- **10M+ activity uploads/month**, with peaks during weekends and challenge periods
- **Billions of data points/month** (GPS, elevation, heart rate, motion)
- **500K+ concurrent users** during peak periods

### Engagement

- **Millions of daily feed interactions** (likes, comments, shares)
- **High-throughput real-time notifications** and leaderboard updates
- **Burst traffic support** for uploads and challenge processing

---

## Architectural Implications

These business and usage patterns require an architecture that is:

- **Optimized for read-heavy workloads**, especially on feeds and leaderboards
- **Resilient to bursty traffic** from activity uploads and challenge participation
- **Built for asynchronous processing** of GPS data, segment matching, and social updates
- **Modular and evolvable**, enabling rapid rollout of new features without affecting core functionality


