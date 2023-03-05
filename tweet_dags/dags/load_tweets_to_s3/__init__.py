import os
from argparse import Namespace
from pprint import pprint
from typing import List

import pandas as pd
from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_s3.config import (
    ENV_VAR_NAMES,
    PARAM_NAMES
) 
from tweet_dags.dags.load_tweets_to_s3.tasks import (
    validate_env_variables,
    validate_params,
    get_tweet_scratch_dir_path,
    validate_tweet_scratch_files,
    get_tweet_source_info,
    get_existing_tweets_from_s3,
    check_for_existing_source_section_title_pages
)
from tweet_dags.dags.load_tweets_to_s3.data_classes import TweetSourceInfo





@log_performance_time(service_name=SERVICE_NAME)
def load_tweets_to_s3(args: Namespace) -> None:
    validate_env_variables(ENV_VAR_NAMES)
    validate_params(args, PARAM_NAMES)
    tweet_scratch_dir_path: str = get_tweet_scratch_dir_path(args.tweet_scratch_dir_path)
    validate_tweet_scratch_files(tweet_scratch_dir_path)
    tweet_source_info: TweetSourceInfo = get_tweet_source_info(tweet_scratch_dir_path)
    existing_tweets: pd.DataFrame = get_existing_tweets_from_s3()
    check_for_existing_source_section_title_pages(tweet_source_info, existing_tweets)
    # new_tweets: pd.DataFrame = transform_tweets_from_scratch_dir(tweet_scratch_dir_path, tweet_source_info)
    # tweets: pd.concat(existing_tweets, new_tweets)
    # validate_tweet_count(tweets, existing_tweets, new_tweets)
    # upload_tweets_to_s3(tweets)