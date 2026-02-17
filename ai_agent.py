import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from agent import (
    assign_mission,
    release_resources,
    show_available_pilots,
    show_available_drones
)

# Load .env locally
load_dotenv()

# Get API key (works both locally and on Streamlit Cloud)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


SYSTEM_PROMPT = """
You are a drone operations coordinator AI.

You help assign pilots, release drones, and answer operational questions.

Interpret user intent and call the correct function.
"""
def interpret_command(user_input):

    text = user_input.lower()

    # ASSIGNMENT INTENT
    if any(word in text for word in ["assign", "allocate", "send", "deploy"]):

        for mission in ["PRJ001", "PRJ002", "PRJ003"]:
            if mission.lower() in text:
                return assign_mission(mission)

        return "Please specify mission ID (example: PRJ001)"


    # SHOW PILOTS INTENT
    if any(word in text for word in ["pilot", "who is available", "available people", "available pilots"]):

        return show_available_pilots()


    # SHOW DRONES INTENT
    if any(word in text for word in ["drone", "available drones", "which drones"]):

        return show_available_drones()


    # RELEASE INTENT
    if any(word in text for word in ["release", "free", "unassign"]):

        words = user_input.upper().split()

        pilot = next((w for w in words if w.startswith("P")), None)
        drone = next((w for w in words if w.startswith("D")), None)

        if pilot and drone:
            return release_resources(pilot, drone)

        return "Specify pilot and drone IDs (example: release P001 D001)"


    # FALLBACK TO OPENAI CHAT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a drone operations assistant.
You help with drone missions, pilots, and assignments.
If you don't have system data, ask the user for clarification.
"""
            },
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
