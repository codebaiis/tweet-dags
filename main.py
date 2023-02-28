import logging
import os
from argparse import ArgumentParser, Namespace
from datetime import date, datetime
from typing import Callable, List

from baiis_utils.decorators import log_performance_time
from dotenv import load_dotenv

from tweet_dags import dags
from tweet_dags.config import SERVICE_NAME



@log_performance_time(service_name=SERVICE_NAME)
def run(args: Namespace) -> None:
    logging.basicConfig(level=logging.INFO)
    dag_name: str = args.dag
    dag_func: Callable[[Namespace], None] = getattr(dags, dag_name)

    # try:
    dag_func(args)
    # except Exception as e:
    #     error_msg: str = f' - {SERVICE_NAME} - ERROR: {e}\n\n{args}'
    #     logging.error(error_msg)





if __name__ == "__main__":
    load_dotenv()
    project_description: str = 'Tweet DAG Suite.'
    parser: ArgumentParser = ArgumentParser(description=project_description)

    parser.add_argument(
        "dag", 
        type=str,
        choices=[ 
            'get_google_sheets_creds',
            'load_tweets_to_google_sheet',
            'load_tweets_to_s3',
        ],
        help="The DAG that will run."
    )


    # load_tweets_to_google_sheet

    parser.add_argument(
        "-ts", "--tweet_scratch_dir_path", 
        dest="tweet_scratch_dir_path", 
        type=str,
        default='default',
        help="The directory where your tweet_scratch files are stored."
    )

    args: Namespace = parser.parse_args()

    run(args)