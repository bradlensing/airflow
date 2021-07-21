import datetime

from airflow import DAG

from operators.has_rows import HasRowsOperator
from operators.s3_to_redshift import S3ToRedshiftOperator
from operators.facts_caculator import FactsCalculatorOperator

# from airflow.operators import (
#     FactsCalculatorOperator,
#     HasRowsOperator,
#     S3ToRedshiftOperator
# )

dag = DAG("3.4-FullDAG", start_date=datetime.datetime.utcnow())

copy_trips = S3ToRedshiftOperator(
    task_id='copy_trips',
    table='trips',
    dag=dag,
    redshift_conn_id='redshift',
    aws_credentials_id='aws_credentials',
    s3_bucket='udacity-dend',
    s3_key='data-pipelines/divvy/unpartitioned/divvy_trips_2018.csv'
)

check_trips = HasRowsOperator(
    task_id='check_trips',
    dag=dag,
    redshift_conn_id='redshift',
    table='trips'
)

calculate_facts = FactsCalculatorOperator(
    task_id="calculate_facts_trips",
    dag=dag,
    redshift_conn_id="redshift",
    origin_table="trips",
    destination_table="trips_facts",
    fact_column="tripduration",
    groupby_column="bikeid"
)

copy_trips >> check_trips
check_trips >> calculate_facts
