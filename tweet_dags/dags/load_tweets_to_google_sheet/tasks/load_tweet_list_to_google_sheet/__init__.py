import logging
import os
from typing import List
from pprint import pprint

from baiis_utils.decorators import log_performance_time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

from tweet_dags.config import SERVICE_NAME





@log_performance_time(service_name=SERVICE_NAME)
def load_tweet_list_to_google_sheet(
        tweets: List[list],
        google_sheet_credentials: Credentials,
        spreadsheet_range: str = 'tweets!A1:J1'
    ) -> None:
    
    service: Resource = build('sheets', 'v4', credentials=google_sheet_credentials, cache_discovery=False)
    sheet: Resource = service.spreadsheets()
    spreadsheet_id: str = os.getenv('GOOGLE_SHEET_SPREADSHEET_ID')

    response = sheet.values().append(
            spreadsheetId=spreadsheet_id, 
            range=spreadsheet_range, 
            valueInputOption='USER_ENTERED', 
            insertDataOption='INSERT_ROWS', 
            body={'values': tweets}
        ) \
        .execute()


    new_row_count: int = response.get('updates').get('updatedRows')
    logging.info(f'    - {new_row_count} new rows were added to spreadsheet {spreadsheet_id}.')