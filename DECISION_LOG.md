# Decision Log — Skylark Drone Operations Coordinator AI Agent

## Overview

This document outlines the design decisions, assumptions, trade-offs, and interpretations made while implementing the Drone Operations Coordinator AI Agent.

---

## Key Assumptions

### 1. Google Sheets as Source of Truth

Google Sheets was treated as the primary database because:

- It satisfies assignment requirements
- Enables easy real-time sync
- Allows manual verification and updates

---

### 2. Pilot Assignment Criteria

Pilots are assigned only if they satisfy all constraints:

- Available status
- Required skills match
- Required certifications match
- Same location as mission
- Within mission budget

This ensures safe and realistic assignments.

---

### 3. Drone Assignment Criteria

Drones are assigned based on:

- Availability
- Capability match with mission skill
- Weather compatibility
- Location match
- Maintenance status

Example:

Rainy missions require IP43-rated drones.

---

### 4. Capability Mapping

Mission skills were mapped to drone capabilities:

- Mapping → LiDAR, RGB
- Inspection → RGB
- Thermal → Thermal

This ensures correct drone selection.

---

## Conflict Detection Design

Conflict detection is handled before assignment to prevent unsafe or invalid assignments.

Conflicts detected include:

- Pilot unavailable
- Drone unavailable
- Drone under maintenance
- Budget overrun
- Location mismatch
- Weather incompatibility
- Certification mismatch

Assignments proceed only if no conflicts exist.

---

## Urgent Reassignment Interpretation

Urgent reassignment was interpreted as:

Automatically attempting assignment using the same assignment logic, prioritizing available and eligible resources immediately.

This ensures urgent missions receive immediate coordination.

If no suitable resources exist, the system safely reports unavailability instead of forcing unsafe assignments.

---

## Technology Choices

### Streamlit

Chosen because:

- Fastest way to build conversational UI
- Built-in hosting support
- Minimal frontend complexity

Trade-off:
Less customizable than full frontend frameworks.

---

### Rule-Based Matching vs Machine Learning

Rule-based logic was used instead of ML because:

- Deterministic and predictable
- Easier to debug and validate
- Faster to implement within time constraints

Trade-off:
Less adaptive compared to ML models.

---

### Google Sheets vs Database

Google Sheets chosen because:

- Assignment explicitly required it
- Easier deployment and testing
- Built-in accessibility

Trade-off:
Less scalable than production databases.

---

## Error Handling Approach

The system safely handles:

- No available pilots
- No available drones
- Conflicting assignments
- Invalid mission requests

Instead of forcing assignments, the agent reports issues clearly.

---

## Deployment Decisions

Streamlit Cloud was chosen because:

- Fast deployment
- Free hosting
- Easy GitHub integration
- Secure secrets management

---

## What Would Be Improved With More Time

- Natural language understanding using LLM
- Automated scheduling optimization
- Distance-based assignment optimization
- Real-time notifications
- Full FastAPI backend
- Role-based access control

---

## Final Outcome

The agent successfully fulfills all assignment requirements:

- Pilot roster management
- Drone inventory tracking
- Assignment coordination
- Conflict detection
- Urgent reassignment handling
- Google Sheets integration
- Conversational interface
- Hosted deployment

