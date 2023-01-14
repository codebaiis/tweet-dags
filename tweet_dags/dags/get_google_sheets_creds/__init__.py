from argparse import Namespace

from baiis_utils.decorators import log_performance_time
from google.oauth2.credentials import Credentials

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_google_sheet.tasks import get_google_sheets_credentials





@log_performance_time(service_name=SERVICE_NAME)
def get_google_sheets_creds(args: Namespace) -> Credentials:
    google_sheet_credentials: Credentials = get_google_sheets_credentials()
    return google_sheet_credentials