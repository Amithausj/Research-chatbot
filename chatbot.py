import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Load the research data from Google Sheets
def load_research_data():
    # Define the scope of the access
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authenticate using the service account
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet by its ID
    sheet_id = "1hW_bA68L51QeNLtgM7t8bOc5X02ZtnUuX6uHiBM5M5Q"  # Your Google Sheet ID
    sheet = client.open_by_key(sheet_id).sheet1  # Access the first sheet (replace if needed)

    # Get all records from the sheet
    data = sheet.get_all_records()

    # Convert the data to a pandas DataFrame
    return pd.DataFrame(data)

# Step 2: Define the function to search all columns
def get_research_info(query, data):
    # Convert the query to lowercase to ensure case-insensitive matching
    query = query.lower()

    # Step 2.1: Search across all columns
