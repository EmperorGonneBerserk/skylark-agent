# Skylark Drone Operations Coordinator AI Agent 🚁

## Overview

This project implements an AI-powered Drone Operations Coordinator that automates pilot assignment, drone allocation, inventory tracking, and conflict detection. It integrates directly with Google Sheets to maintain real-time synchronization and provides a conversational interface for managing operations.

This system replaces manual coordination workflows with an intelligent agent capable of making safe, constraint-aware decisions.

---

## Hosted Prototype

Live App: https://skylark-agent-letbnr7dnkksuor5kmeynz.streamlit.app/

GitHub Repository: https://github.com/EmperorGonneBerserk/skylark-agent

---

## Features

### 1. Pilot Roster Management

- View available pilots
- Filter pilots by:
  - skills
  - certifications
  - location
  - availability
- Update pilot assignment status automatically
- Calculate assignment eligibility based on budget

---

### 2. Drone Fleet Management

- View available drones
- Filter drones by:
  - weather resistance
  - capability
  - maintenance status
  - location
- Prevent assignment of drones under maintenance

---

### 3. Intelligent Assignment Engine

Automatically assigns the best:

- Pilot based on:
  - skills match
  - certification match
  - availability
  - location
  - budget constraints

- Drone based on:
  - mission requirements
  - weather compatibility
  - availability
  - location

---

### 4. Conflict Detection System

Detects and prevents:

- Assigning unavailable pilots
- Assigning drones in maintenance
- Weather incompatibility risks
- Certification mismatches
- Budget overruns
- Location mismatches

---

### 5. Urgent Reassignment Handling

The agent can automatically reassign pilots and drones when urgent missions arise, selecting the best available resources while maintaining safety and constraint compliance.

---

### 6. Conversational Interface

Users interact using simple commands:

Example commands:

show available pilots
show available drones
assign PRJ001
urgent PRJ002


---

### 7. Google Sheets Integration (2-Way Sync)

The system uses Google Sheets as the database.

Reads:

- Pilot roster
- Drone fleet
- Mission list

Writes:

- Pilot status updates
- Drone assignment updates

This ensures real-time synchronization.

---
## Conversational AI Integration (OpenAI)

The system now supports natural language interaction using OpenAI's GPT model. Instead of requiring fixed commands, users can interact conversationally.

Examples:

- "Assign someone to PRJ001"
- "Who is available right now?"
- "Do we have drones that can operate in rain?"
- "Release pilot P001 and drone D001"

### How it works

The conversational layer is implemented in `ai_agent.py`. It performs:

1. Intent detection from user input
2. Routing to the correct backend function
3. Executing assignment, release, or query logic
4. Returning structured results to the user

This enables a flexible and intuitive coordination interface.

---

## Resource Lifecycle Management

To ensure continuous system usability, resource release functionality was implemented.

Users can release assigned resources manually:

Example:

release P001 D001


This updates Google Sheets and makes the pilot and drone available again.

This prevents permanent assignment locking and ensures the system remains operational indefinitely.

---

## Intent Routing Architecture

The AI agent uses a hybrid architecture combining:

- Deterministic intent routing (for assignment, release, availability)
- OpenAI conversational fallback (for general questions)

This ensures:

- Reliable execution of critical operations
- Natural conversational flexibility
- Prevention of hallucinated assignments

---

## Architecture

User
↓
Streamlit UI (app.py)
↓
Conversational AI Layer (ai_agent.py)
↓
Coordinator Logic (agent.py)
↓
Assignment Engines (assignment.py, drone_assignment.py)
↓
Conflict Detection (conflict_detection.py)
↓
Database Layer (sheets.py)
↓
Google Sheets

---

## AI Agent File Overview

| File | Role |
|----|----|
| app.py | Streamlit user interface |
| ai_agent.py | Conversational AI interpreter and intent router |
| agent.py | Core coordinator logic |
| assignment.py | Pilot selection engine |
| drone_assignment.py | Drone selection engine |
| conflict_detection.py | Assignment safety validation |
| sheets.py | Google Sheets integration |
| test_*.py | Unit tests |

---

## Security

Sensitive credentials are stored securely using:

- `.env` file (local development)
- Streamlit Secrets Manager (production deployment)

Credentials are never committed to version control.

---

## Example Workflow

Example interaction:

User: Assign someone to PRJ001

System:
Mission Assigned Successfully
Pilot: Arjun
Drone: D001
Location: Bangalore

User: Release P001 D001

System:
Pilot P001 and Drone D001 released successfully.

## Installation (Local Setup)

Clone repo:



git clone https://github.com/EmperorGonneBerserk/skylark-agent.git

cd skylark-agent


Create virtual environment:

Create a .env file and then configure the openai api key


python -m venv venv
venv\Scripts\activate


Install dependencies:



pip install -r requirements.txt


Add credentials.json file.

Run app:



streamlit run app.py


---

## Deployment

Hosted on Streamlit Cloud.

Secrets configured securely using Streamlit Secrets Manager.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Google Sheets API
- gspread
- OAuth2 Service Accounts
- OPENAI

---

## Key Capabilities Demonstrated

- Intelligent resource allocation
- Constraint-aware decision making
- Conflict detection and prevention
- Real-time database synchronization
- Conversational AI coordination interface

---

## Author

Shushruth Gowda
