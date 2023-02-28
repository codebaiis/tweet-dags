import os

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME





@log_performance_time(service_name=SERVICE_NAME)
def get_tweet_scratch_dir_path(dir_path: str) -> str:
    if dir_path == 'default':
        dir_path = os.path.join('tweet_dags', 'dags', 'load_tweets_to_s3', 'tweet_scratch')
    return dir_path