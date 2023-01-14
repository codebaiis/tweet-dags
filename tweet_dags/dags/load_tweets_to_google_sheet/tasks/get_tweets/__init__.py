import os
from typing import List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME
from tweet_dags.dags.load_tweets_to_google_sheet.tasks.get_tweet_source_info.data_classes import TweetSourceInfo
from tweet_dags.dags.load_tweets_to_google_sheet.tasks.get_tweets.data_classes import Tweet



@log_performance_time(service_name=SERVICE_NAME)
def get_tweets_from_scratch_dir(
        tweet_scratch_dir_path: str, 
        tweet_source_info: TweetSourceInfo,
        tweet_scratch_filename: str = 'tweets_scratch.md',
        caption_identifier: str = '####'
    ) -> List[Tweet]:
    
    tweets: List[Tweet] = []
    filepath: str = os.path.join(tweet_scratch_dir_path, tweet_scratch_filename)

    with open(filepath, 'r') as file_handler:
        threads: List[str] = file_handler.read().split('\n\n\n')

    for thread_num, thread in enumerate(threads, start=1):
        contents: List[str] = thread.split('\n\n')
        contents = [content.strip() for content in contents if content]
        for thread_order_num, content in enumerate(contents, start=1):
            # print(thread_num, thread_order_num, '/', len(contents), content)
            thread_caption: bool = False 

            if caption_identifier in content:
                thread_caption = True
                content = content.replace(caption_identifier, '') 

            tweet: Tweet = Tweet(
                    content,
                    thread_num,
                    thread_order_num,
                    thread_caption,
                    tweet_source_info.author,
                    tweet_source_info.title,
                    tweet_source_info.section_title,
                    tweet_source_info.link,
                    tweet_source_info.tags,
                    tweet_source_info.pages
                )
            tweets.append(tweet)
            
            
    return tweets