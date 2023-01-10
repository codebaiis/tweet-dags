# tweet-dags
DAGs for composing and sharing small bits of info (tweets)


## DAGs
<details>
    <summary>load_tweets_to_google_sheet</summary>

    tasks:

    1. validate_env_variables
    2. validate_params
    3. get_tweet_scratch_dir_path
    4. validate_tweet_scrath_files
    5. get_tweet_source_info
    6. get_google_sheets_credentials
    7. check_for_existing_source_section_title_pages
    8. get_tweets_from_scratch_dir

</details>


*** 

## How To
<details>
    <summary>run w/ Docker</summary>
    
    1. update the command in `run.sh` with the correct dag name and arguments.

    2. run the following commands to build and run the docker image
    ```bash
        docker build --tag tweet_dags .
        docker run --env-file .env tweet_dags
    ```

</details>

***

<details>
    <summary>To Do</summary>

    - add `get_google_sheet_credentials()` DAG that calls the existing function of the same name 
        - add notes on how to run to get new credentials once existing credentials have expired
    - see if I can optimize `check_for_existing_source_section_title_pages()`
        - add a `source_section_title_spreadsheet_range` argument and remove as an environment variable

</details>

