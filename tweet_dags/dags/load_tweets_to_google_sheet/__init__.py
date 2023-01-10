import os
from argparse import Namespace
from typing import List

from baiis_utils.decorators import log_performance_time
from google.oauth2.credentials import Credentials

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_google_sheet.tasks import (
    validate_env_variables,
    validate_params,
    get_tweet_scratch_dir_path,
    validate_tweet_scrath_files,
    get_tweet_source_info,
    get_google_sheets_credentials,
    check_for_existing_source_section_title_pages,
    get_tweets_from_scratch_dir,
)
from tweet_dags.dags.load_tweets_to_google_sheet.data_classes import (
    TweetSourceInfo,
    Tweet
)




@log_performance_time(service_name=SERVICE_NAME)
def load_tweets_to_google_sheet(args: Namespace) -> None:
    validate_env_variables()
    validate_params(args)
    tweet_scratch_dir_path: str = get_tweet_scratch_dir_path(args.tweet_scratch_dir_path)
    validate_tweet_scrath_files(tweet_scratch_dir_path)
    tweet_source_info: TweetSourceInfo = get_tweet_source_info(tweet_scratch_dir_path)
    google_sheet_credentials: Credentials = get_google_sheets_credentials()
    check_for_existing_source_section_title_pages(tweet_source_info, google_sheet_credentials)
    tweets_from_scatch_dir: List[Tweet] = get_tweets_from_scratch_dir(tweet_scratch_dir_path, tweet_source_info)
    