import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator

def greet():
    logging.info("Hello World")

dag = DAG(
    'lesson1.demo1',
    start_date=datetime.datetime.now()
)

greet_task = PythonOperator(
    task_id='greet_task',
    python_callable=greet,
    dag=dag
)