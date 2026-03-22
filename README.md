
# SentinelConfig 

A high-performance, distributed feature flag and dynamic configuration service designed for cloud-native environments.

## Overview
SentinelConfig allows engineering teams to manage application behavior in real-time without redeploying code. It focuses on low-latency configuration delivery and high availability.

### Key Engineering Concepts
*   **Distributed Caching:** Implements the Read-Aside pattern with Redis to achieve sub-50ms lookup latency.
*   **Consistency vs. Availability:** Uses PostgreSQL as the source of truth with write-through invalidation for the cache layer.
*   **Infrastructure as Code:** Automated environment provisioning using Docker and (planned) Terraform.
*   **Real-time Propagation:** (In-Progress) Utilizing WebSockets for instant configuration updates to client SDKs.

## Tech Stack
*   **Backend:** Python (FastAPI), SQLAlchemy (ORM)
*   **Databases:** PostgreSQL (Primary), Redis (Cache)
*   **DevOps:** Docker, Docker Compose, GitHub Actions (CI/CD)
*   **Frontend:** React (Admin Dashboard - Planned)

## Quick Start (Local Development)
1. Ensure you have Docker and Python 3.10+ installed.
2. `docker-compose up --build`
3. Access the API documentation at `http://localhost:8000/docs`# sentinel-config
