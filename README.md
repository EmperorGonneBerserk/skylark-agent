# Skylark Drone Operations Coordinator AI Agent 🚁

## Overview

This project implements an AI-powered Drone Operations Coordinator that automates pilot assignment, drone allocation, inventory tracking, and conflict detection. It integrates directly with Google Sheets to maintain real-time synchronization and provides a conversational interface for managing operations.

This system replaces manual coordination workflows with an intelligent agent capable of making safe, constraint-aware decisions.

---

## Hosted Prototype

Live App: https://YOUR-STREAMLIT-LINK.streamlit.app

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

## Architecture



Streamlit UI
↓
Agent Layer (agent.py)
↓
Assignment Engine (assignment.py, drone_assignment.py)
↓
Conflict Detection (conflict_detection.py)
↓
Database Layer (sheets.py)
↓
Google Sheets


---

## Project Structure



skylark-agent/
│
├── app.py
├── agent.py
├── sheets.py
├── assignment.py
├── drone_assignment.py
├── conflict_detection.py
│
├── test_agent.py
├── test_assignment.py
├── test_conflicts.py
├── test_drone_assignment.py
├── test_sheets.py
├── test_sync.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## Installation (Local Setup)

Clone repo:



git clone https://github.com/EmperorGonneBerserk/skylark-agent.git

cd skylark-agent


Create virtual environment:



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