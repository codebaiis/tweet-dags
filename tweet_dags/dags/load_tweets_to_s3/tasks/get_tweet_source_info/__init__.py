import json
import os 
from typing import Dict, List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_s3.tasks.get_tweet_source_info.data_classes import TweetSourceInfo



@log_performance_time(service_name=SERVICE_NAME)
def get_tweet_source_info(
        tweet_scratch_dir_path: str,
        tweet_source_info_filename: str = 'tweets_source_info.json'
    ) -> TweetSourceInfo:
    
    filepath: str = os.path.join(tweet_scratch_dir_path, tweet_source_info_filename)
    
    with open(filepath, 'r') as file_handler:
        source_data: Dict = json.load(file_handler)

    tweet_source_info: TweetSourceInfo = TweetSourceInfo(**source_data)
    invalid_fields: List[str] = tweet_source_info.get_invalid_fields()
    if invalid_fields:
        error_msg: str = f'the following fields are invalid in {filepath}:\n{invalid_fields}'
        raise Exception(error_msg)
    return tweet_source_info


    
