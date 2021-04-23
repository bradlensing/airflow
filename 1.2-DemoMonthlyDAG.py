import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator

def greet():
    logging.info("Hello World Monthly")

dag = DAG(
    dag_id='demo_monthly',
    start_date=datetime.datetime.now() - datetime.timedelta(days=65),
    schedule_interval="@monthly"
)

greet_task = PythonOperator(
    task_id='greet_task',
    python_callable=greet,
    dag=dag
)