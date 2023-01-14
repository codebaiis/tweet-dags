import os
from typing import Dict, List

from baiis_utils.decorators import log_performance_time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_google_sheet.tasks.get_tweet_source_info.data_classes import TweetSourceInfo
from tweet_dags.dags.load_tweets_to_google_sheet.tasks.get_google_sheet_credentials import get_google_sheets_credentials






@log_performance_time(service_name=SERVICE_NAME)
def check_for_existing_source_section_title_pages(
        tweet_source_info: TweetSourceInfo,
        google_sheet_credentials: Credentials,
        source_section_title_spreadsheet_range: str = 'tweets!G2:H'
    ) -> List[str]:

    section_title: str = tweet_source_info.section_title
    pages: str = tweet_source_info.pages
    source_section_title_page: List[str,str] = [section_title, pages]

    service: Resource = build('sheets', 'v4', credentials=google_sheet_credentials, cache_discovery=False)
    sheet: Resource = service.spreadsheets()

    spreadsheet_id: str = os.getenv('GOOGLE_SHEET_SPREADSHEET_ID')

    result: Dict = sheet.values().get(
                spreadsheetId=spreadsheet_id,
                range=source_section_title_spreadsheet_range
            ).execute()

    existing_source_section_title_pages: List[List[str,str]] = result.get('values', [])
    if source_section_title_page in existing_source_section_title_pages:
        error_msg: str = f'  - tweets for section "{section_title} {"pg" if pages else ""} {pages if pages else ""}" have already been added to googlesheet {spreadsheet_id}'
        raise Exception(error_msg)

    
