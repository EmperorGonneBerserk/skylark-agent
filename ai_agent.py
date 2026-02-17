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

    # Direct intent handling first (fast and reliable)
    if "assign" in text or "mission" in text:

        for m in ["PRJ001", "PRJ002", "PRJ003"]:
            if m.lower() in text:
                return assign_mission(m)

        return "Please specify mission ID (example: PRJ001)"

    elif "available pilot" in text:
        return show_available_pilots()

    elif "available drone" in text:
        return show_available_drones()

    elif "release" in text:

        words = user_input.upper().split()

        pilot = next((w for w in words if w.startswith("P")), None)
        drone = next((w for w in words if w.startswith("D")), None)

        if pilot and drone:
            return release_resources(pilot, drone)

        return "Specify pilot and drone IDs"

    # Fallback to OpenAI conversational response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
