from dagster import  job
from dagster_home.main import main

@job
def job_main():
    main()