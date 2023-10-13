import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
import csv

def main(csv_file):
    CREDENTIALS_FILE = 'google_credentials.json'

    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERROR: Credentials file not found: {CREDENTIALS_FILE}")
        return 403
    
    if not os.path.exists(csv_file):
        print(f"ERROR: CSV file not found: {csv_file}")
        return 412


    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)
    sheets_service = build('sheets', 'v4', credentials=creds)

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    creds = creds.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])

    spreadsheet_id = '1DMYPQIDez7wZPKcl89HNI4uKEn6NjDbNxHRhmr_nLc4'

    if not spreadsheet_id:
        spreadsheet = sheets_service.spreadsheets().create(
            body={'properties': {'title': 'Testing Spreadsheet'}}
        ).execute()
        spreadsheet_id = spreadsheet['spreadsheetId']

    body = {
        'values': data
    }

    result = sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Sheet1',  # Replace with the name or range of your choice
        valueInputOption='RAW',
        body=body
    ).execute()

    print('Data added to Google Sheet.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <csv_file.csv>')
    else:
        csv_file = sys.argv[1]
        main(csv_file)