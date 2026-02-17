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

## Conversational AI Design Decision

Initially, the system supported fixed command inputs such as:

- assign PRJ001
- show available pilots

To improve usability and meet the conversational interface requirement more effectively, OpenAI's GPT model was integrated.

A hybrid architecture was chosen:

- Deterministic intent routing for critical operations
- OpenAI fallback for conversational responses

This ensures operational safety while allowing natural language interaction.

Example supported inputs:

- "Assign someone to PRJ001"
- "Who is available right now?"
- "Release P001 and D001"

---

## Intent Routing vs Fully Autonomous LLM

A fully autonomous LLM-controlled system was considered but rejected due to safety risks.

Instead, intent routing was implemented:

LLM → Intent detection → Controlled backend function execution

This prevents:

- Invalid assignments
- Hallucinated operations
- Unsafe system actions

This design ensures reliability and predictability.

---

## Resource Lifecycle Management Decision

Initially, once pilots and drones were assigned, they remained permanently assigned.

This caused system resource exhaustion.

To solve this, explicit resource release functionality was implemented.

Release command:

release P001 D001


This allows continuous system operation and realistic lifecycle management.

This mirrors real-world operations where resources are reused after mission completion.

---

## Separation of Concerns Architecture

The system was structured into layers:

- UI Layer (Streamlit)
- Conversational AI Layer
- Coordination Logic Layer
- Assignment Engines
- Conflict Detection Layer
- Database Layer

This modular architecture improves:

- Maintainability
- Testability
- Scalability

---

## Unit Testing Strategy

Unit tests were created for each major subsystem:

- Google Sheets connectivity
- Pilot assignment logic
- Drone assignment logic
- Conflict detection
- Full coordinator flow

This ensured correctness of each component independently before integration.

---

## Deployment and Secrets Management

Sensitive credentials were managed using:

- Local: `.env`
- Production: Streamlit Secrets

This prevents credential exposure while enabling secure deployment.

---

## Final System Capabilities

The system now supports:

- Natural language mission assignment
- Intelligent pilot and drone selection
- Conflict detection and prevention
- Resource lifecycle management
- Real-time Google Sheets synchronization
- Hosted conversational interface

This fulfills all assignment requirements and provides production-level functionality.

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

