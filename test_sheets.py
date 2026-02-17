import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

spreadsheet = client.open("Skylark Drones Database")

pilot_sheet = spreadsheet.worksheet("PilotRoster")

data = pilot_sheet.get_all_records()

print(data)
