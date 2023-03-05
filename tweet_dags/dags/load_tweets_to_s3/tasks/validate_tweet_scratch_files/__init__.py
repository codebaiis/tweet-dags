import os
from datetime import datetime, timedelta
from typing import List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME



FILE_EXPIRATION_MINUTES: int = 600


@log_performance_time(service_name=SERVICE_NAME)
def validate_tweet_scratch_files(
        tweet_scratch_dir_path: str,
        tweet_scratch_filename: str = 'tweets_scratch.md',
        tweet_source_info_filename: str = 'tweets_source_info.json'
    ) -> None:

    file_expiration: datetime = datetime.now() - timedelta(minutes=FILE_EXPIRATION_MINUTES)

    filenames: List[str] = [tweet_scratch_filename, tweet_source_info_filename]
    for filename in filenames:
        filepath: str = os.path.join(tweet_scratch_dir_path, filename)
        file_last_modified: datetime = datetime.fromtimestamp(os.path.getmtime(filepath))
        if file_last_modified < file_expiration:
            error_msg: str = f'{filepath} has not been update in the last {FILE_EXPIRATION_MINUTES} minutes. Please update.'
            raise Exception(error_msg)