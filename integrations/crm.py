import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def export_csv(lead_dict, path="lead_export.csv"):
    df = pd.DataFrame([lead_dict])
    # append to file or create if missing
    try:
        df2 = pd.read_csv(path)
        df = pd.concat([df2, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv(path, index=False)



def append_to_sheet(json_credentials_path, spreadsheet_name, row):
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_credentials_path,
        ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)
    sheet = client.open(spreadsheet_name).sheet1
    sheet.append_row(row)
