import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator

def greet3():
    logging.info("Hello World from 3 Months")

dag = DAG(
    dag_id='Demo3MonthDag',
    start_date=datetime.datetime.now() - datetime.timedelta(days=95),
    schedule_interval="@monthly"
)

greet_task = PythonOperator(
    task_id='greet_for_3_months',
    python_callable=greet3,
    dag=dag
)