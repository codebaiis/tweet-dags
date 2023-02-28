import os
from argparse import Namespace
from typing import List

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
    validate_tweet_scratch_files
)





@log_performance_time(service_name=SERVICE_NAME)
def load_tweets_to_s3(args: Namespace) -> None:
    validate_env_variables(ENV_VAR_NAMES)
    validate_params(args, PARAM_NAMES)
    tweet_scratch_dir_path: str = get_tweet_scratch_dir_path(args.tweet_scratch_dir_path)
    validate_tweet_scratch_files(tweet_scratch_dir_path)