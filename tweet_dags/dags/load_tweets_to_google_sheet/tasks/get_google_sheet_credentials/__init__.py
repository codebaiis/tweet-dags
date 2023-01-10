from __future__ import print_function

import os.path

from baiis_utils.decorators import log_performance_time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import RefreshError

from tweet_dags.config import SERVICE_NAME







@log_performance_time(service_name=SERVICE_NAME)
def get_google_sheets_credentials(
        google_sheets_token_file_path: str = os.path.join('tweet_dags', 'config', 'google_sheets_token.json'),
        google_sheets_credentials_file_path: str = os.path.join('tweet_dags', 'config', 'google_sheets_credentials.json')
    ) -> Credentials:

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds: Credentials = None

    if os.path.exists(google_sheets_token_file_path):
        creds = Credentials.from_authorized_user_file(google_sheets_token_file_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                flow = InstalledAppFlow.from_client_secrets_file(google_sheets_credentials_file_path, SCOPES)
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(google_sheets_credentials_file_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(google_sheets_token_file_path, 'w') as token:
            token.write(creds.to_json())

    return creds