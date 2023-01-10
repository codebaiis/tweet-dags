from argparse import Namespace
from typing import Dict, List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME




@log_performance_time(service_name=SERVICE_NAME)
def validate_params(args: Namespace) -> None:
    params: Dict = {
        'tweet_scratch_dir_path': args.tweet_scratch_dir_path,

    }

    missing_params: List[str] = []

    for param_name, param_val in params.items():
        if not param_val:
            missing_params.append(param_name)

    try:
        assert len(missing_params) == 0
    except AssertionError:
        raise AssertionError(f'the following parameters need to be passed in:\n {missing_params}')