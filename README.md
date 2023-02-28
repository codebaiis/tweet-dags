# tweet-dags
DAGs for composing and sharing small bits of info (tweets)


## DAGs
<details>
    <summary>load_tweets_to_google_sheet</summary>

    tasks:

    1. validate_env_variables
    2. validate_params
    3. get_tweet_scratch_dir_path
    4. validate_tweet_scratch_files
    5. get_tweet_source_info
    6. get_google_sheets_credentials
    7. check_for_existing_source_section_title_pages
    8. get_tweets_from_scratch_dir
    9. load_tweet_list_to_google_sheet

</details>


<details>
    <summary>get_google_sheet_creds</summary>

    tasks:

    1. get_google_sheets_credentials

</details>

<details>
    <summary>load_tweets_to_s3</summary>

    tasks:

    1. validate_env_variables
    2. validate_params
    3. get_tweet_scratch_dir_path
    4. validate_tweet_scratch_files
    5. get_tweet_source_info
    6. download_tweets_csv_from_s3
    7. check_for_existing_source_section_title_pages
    8. get_tweets_from_scratch_dir
    9. add_tweets_to_csv
    10. upload_tweets_csv_to_s3

</details>


*** 

## How To
<details>
    <summary>run locally</summary>
    
    1. create/activate a virtual environment
    2. `pip install wheel`
    3. `python setup.py bdist_wheel`
    4. `pip3 install dist/*.whl`
    5. update the command in `run.sh` with the correct dag name and arguments.
    6. `source run.sh` 
    ```

</details>

<details>
    <summary>run w/ Docker</summary>
    
    1. update the command in `run.sh` with the correct dag name and arguments.

    2. run the following commands to build and run the docker image
    ```bash
        docker build --tag tweet_dags .
        docker run --env-file .env tweet_dags
    ```

</details>

<details>
    <summary>update google sheet credentials</summary>
    
    There may be times when Google Sheets credentials token (`tweet_dags/config/google_sheets_token.json`) expires and will prevent the DAGs from running. If you receive this error, take these steps:

    1. create and activate a virtual environment
        - we haven't figured out how to update credentials from within a docker container, yet.
    2. `pip install wheel`
    3. `python setup.py bdist_wheel`
    4. `pip install dist/*.whl`
    5. `python3 main.py get_google_sheets_creds`

</details>

***

<details>
    <summary>To Do</summary>

    - load_tweet_list_to_google_sheet(tweets: List[List])
        - https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
        - https://www.youtube.com/watch?v=OZDGVTmQ45Q

</details>

