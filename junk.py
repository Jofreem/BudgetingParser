spreadsheet_id = 'your-spreadsheet-id'

# Specify the destination sheets and starting line numbers
sheet_data = [
    {'sheet_name': 'Sheet1', 'start_line': 2},  # Example: Start at row 2 on Sheet1
    {'sheet_name': 'Sheet2', 'start_line': 5},  # Example: Start at row 5 on Sheet2
    # Add more sheets as needed
]

# Process and write data to Google Sheets
for sheet_info in sheet_data:
    sheet_name = sheet_info['sheet_name']
    start_line = sheet_info['start_line']
    
    # Process data as needed, e.g., filter or modify
    processed_data = data
    
    # Update the Google Sheet with the processed data, starting at the specified line
    body = {
        'values': processed_data
    }
    range_name = f"{sheet_name}!A{start_line}"  # Adjust the column letter as needed
    result = sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f'Data added to {sheet_name} starting at line {start_line}.')