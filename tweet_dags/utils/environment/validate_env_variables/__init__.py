import os
from typing import Dict, List

from baiis_utils.decorators import log_performance_time

from tweet_dags.config import SERVICE_NAME




@log_performance_time(service_name=SERVICE_NAME)
def validate_env_variables(env_var_names: List[str]) -> None:
    missing_env_vars: List[str] = []

    for var_name in env_var_names:
        var_value = os.getenv(var_name)
        if not var_value:
            missing_env_vars.append(var_name)

    try:
        assert len(missing_env_vars) == 0
    except AssertionError:
        raise AssertionError(f'the following environment variables need to be set:\n {missing_env_vars}')

    