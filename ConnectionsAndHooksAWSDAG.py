import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.hooks.S3_hook import S3Hook

# CREATE AWS VARIABLES
# airfow console > Admin > Variables > + New One
    # Key = "s3_bucket" Val = "udacity-dend"
    # Key = "s3_prefix" Val = "data-pipelines"
# CREATE A CONNECTION 
    # airflow console > Admin > Connections > Make New one +
    # Conn Id = aws_credentials, Conn Type = Amazon Web Services, 
    # Login = your aws_acess_key, Password = your aws_secret_key

def list_keys():
    hook = S3Hook(aws_conn_id='aws_credentials')
    bucket = Variable.get('s3_bucket')
    logging.info(f"Listing Keys from {bucket}")
    keys = hook.list_keys(bucket)
    for key in keys:
        logging.info(f" - s3://{bucket}/{key}")

dag = DAG(
    dag_id='connections_hooks_aws',
    start_date=datetime.datetime.now(),
    schedule_interval=None,
    tags=['demo']
)

list_task = PythonOperator(
    task_id='list_task',
    python_callable=list_keys,
    dag=dag
)

