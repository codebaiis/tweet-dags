import os
from typing import List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME





@log_performance_time(service_name=SERVICE_NAME)
def validate_env_variables() -> None:
    
    env_vars = {
        'GOOGLE_SHEET_SPREADSHEET_ID': os.getenv('GOOGLE_SHEET_SPREADSHEET_ID'),
        'GOOGLE_SHEET_SPREADSHEET_RANGE_NAME': os.getenv('GOOGLE_SHEET_SPREADSHEET_RANGE_NAME'),

        # 'SLACK_WEBHOOK_URL': os.getenv('SLACK_WEBHOOK_URL'),
        # 'SLACK_USER_IDS': os.getenv('SLACK_USER_IDS')
    }

    missing_env_vars: List[str] = []

    for var_name, var_val in env_vars.items():
        if not var_val:
            missing_env_vars.append(var_name)

    try:
        assert len(missing_env_vars) == 0
    except AssertionError:
        raise AssertionError(f'the following environment variables need to be set:\n {missing_env_vars}')