import os
from typing import List

import pandas as pd

from tweet_dags.dags.load_tweets_to_s3.data_classes import TweetSourceInfo





def check_for_existing_source_section_title_pages(
        tweet_source_info: TweetSourceInfo, 
        existing_tweets: pd.DataFrame
    ) -> None:
    
    section_title: str = tweet_source_info.section_title
    pages: str = tweet_source_info.pages
    section_title_and_pages: str = f'{section_title} {pages}'.strip()
    existing_section_title_pages: pd.Series = existing_tweets['source_section_title'] + ' ' + existing_tweets['source_pages']
    existing_section_title_pages = existing_section_title_pages.apply(lambda x: x.strip())
    unique_existing_section_title_pages: List[str] = existing_section_title_pages.unique().tolist()
    if section_title_and_pages in unique_existing_section_title_pages:
        s3_bucket: str = os.getenv('AWS_S3_BUCKET')
        s3_file_key: str = os.getenv('AWS_S3_TWEETS_RAW_FILE_KEY')
        error_msg: str = f'  - tweets for section "{section_title} {"pg" if pages else ""} {pages if pages else ""}" have already been added to s3/{s3_bucket}/{s3_file_key}'
        raise Exception(error_msg)