import gspread
import streamlit as st
import pandas as pd
import os
from oauth2client.service_account import ServiceAccountCredentials


# Google Sheets authentication
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
# Try Streamlit secrets first (Cloud), fallback to credentials.json (Local)
try:
    import streamlit as st

    if "gcp_service_account" in st.secrets:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            st.secrets["gcp_service_account"],
            scope
        )
    else:
        raise Exception("No Streamlit secrets found")

except Exception:
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json",
        scope
    )

client = gspread.authorize(creds)

SPREADSHEET_NAME = "Skylark Drones Database"

spreadsheet = client.open(SPREADSHEET_NAME)

# -------------------------
# READ FUNCTIONS
# -------------------------

def get_pilots():

    sheet = spreadsheet.worksheet("PilotRoster")

    data = sheet.get_all_records()

    return pd.DataFrame(data)


def get_drones():

    sheet = spreadsheet.worksheet("DroneFleet")

    data = sheet.get_all_records()

    return pd.DataFrame(data)


def get_missions():

    sheet = spreadsheet.worksheet("Missions")

    data = sheet.get_all_records()

    return pd.DataFrame(data)


# -------------------------
# UPDATE FUNCTIONS
# -------------------------

def update_pilot_status(pilot_id, new_status):

    sheet = spreadsheet.worksheet("PilotRoster")

    records = sheet.get_all_records()

    for i, row in enumerate(records):

        if row["pilot_id"] == pilot_id:

            status_column = list(row.keys()).index("status") + 1

            sheet.update_cell(i + 2, status_column, new_status)

            return True

    return False


def update_drone_status(drone_id, new_status):

    sheet = spreadsheet.worksheet("DroneFleet")

    records = sheet.get_all_records()

    for i, row in enumerate(records):

        if row["drone_id"] == drone_id:

            status_column = list(row.keys()).index("status") + 1

            sheet.update_cell(i + 2, status_column, new_status)

            return True

    return False
