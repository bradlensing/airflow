import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.hooks.S3_hook import S3Hook


def log_details(*args, **kwargs):
    ds = kwargs['ds'] # kwargs[]
    run_id = kwargs['run_id'] # kwargs[]
    previous_ds = kwargs.get('prev_ds') # kwargs.get('')
    next_ds = kwargs.get('next_ds') # kwargs.get('')

    logging.info(f"Execution date is {ds}")
    logging.info(f"My run id is {run_id}")
    if previous_ds:
        logging.info(f"My previous run was on {previous_ds}")
    if next_ds:
        logging.info(f"My next run will be {next_ds}")

dag = DAG(
    dag_id='context_and_templating',
    start_date=datetime.datetime.now() - datetime.timedelta(days=2),
    schedule_interval='@daily',
    tags=['demo']
)

list_task = PythonOperator(
    task_id='details',
    python_callable=log_details,
    provide_context=True,
    dag=dag)