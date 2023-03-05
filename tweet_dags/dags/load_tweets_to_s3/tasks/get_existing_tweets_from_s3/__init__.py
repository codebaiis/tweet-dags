import os

import boto3
import numpy as np
import pandas as pd
from botocore import client






def get_existing_tweets_from_s3() -> pd.DataFrame:
    aws_access_key_id: str = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = os.getenv('AWS_SECRET_ACCESS_KEY')
    s3_bucket_name: str = os.getenv('AWS_S3_BUCKET')
    s3_file_key: str = os.getenv('AWS_S3_TWEETS_RAW_FILE_KEY')
    s3_client: client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    response: dict = s3_client.get_object(Bucket=s3_bucket_name, Key=s3_file_key)
    status: int = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    if status == 200:
        tweets: pd.DataFrame = pd.read_csv(response.get("Body"))
        tweets = tweets.replace(np.nan, '', regex=True)
    else:
        error_msg: str = f'Unsuccessful S3 get_object response. Status - {status}'
        raise Exception(error_msg)
    return tweets