## Using Apache Airflow to build a S3-to-Redshift DAG

### Introduction

The following documentation shows how to build a simple data pipeline that takes data from S3 and loads it into RedShift using Apache Airflow.

### Part 1: Create and Launch an AWS Redshift Cluster

Use these steps in the [S3ToRedshift](./04-Airflow/S3ToRedshift.md) Notebook

### Part 2: Design your Data Pipeline.

DAG is called `S3ToRedshiftDAG`.

This pipeline is generated using the below code. There are 3 essential components of a data pipeline:

- **DAGs** : A DAG is made up of a sequence of operators.
- **Operators**: An operator is basically a task (the rectangle box). The operator makes use of Hooks to connect with external entities like S3, Redshift etc.
  - **PythonOperator**: This takes a callback function which defines the instructions that make up the task.
  - **PostgresOperator**: This takes a sql argument, which when given a SQL statement, it executes it in the task.
- **Hooks**: Think of a hook as getting the connection that you have defined in Airflow.

The structure of the pipeline itself is very easy to layout. Like so:

```
create_table >> copy_task >> location_traffic_task
```

copy_task here is PythonOperator which takes `load_data_to_redshift` as the callback function.

<!-- ![data-pipeline](images/data-pipeline.png) -->

### Callbacks and context variables

It is worth mentioning here, that you can also pass context to the PythonOperator, which essentially allows it to access Airflow's runtime variables (context variables).

```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_date(*args, **kwargs):
    print(f“Hello {kwargs[‘execution_date’]}”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id=’hello_date’,
    python_callable=hello_date,
    provide_context=True,
    dag=divvy_dag)
```

All the context variables:
https://airflow.apache.org/macros.html

### Define S3 and Redshift connections in Airflow

On the left is the `S3 connection`. The Login and password are the IAM user's access key and secret key that you created in part 1. Basically, by using these credentials, we are able to read data from S3.

On the right is the `redshift connection`. These values can be easily gathered from your Redshift cluster in part 1.

<!-- ![connections](images/connections.png) -->

### Define S3 variables for bucket and prefix (so that you don't have to hard code that in the code). Airflow maintains these for us. But we need to create it first.

<!-- ![variables](images/variables.png) -->

### Part 3: Connect to cluster, load data and perform analysis

In the second part, we will be making use of the cluster we just launched in part 1.

You can quickly validate using the redshift console that the tables are created:

<!-- ![validate-on-redshift](images/validate-on-redshift.png) -->

Alternately, you can connect to the redshift cluster from jupyter notebook, as shown below:

Using sql extension, we can directly run SQL commands within jupyter notebook.

- A single `%sql` means the query is a python string accessed using the dollar sign.
- A `%%sql` means the query is not a python string but can be multiline SQL statements

## Part 4: Clean up resources

<b><font color='red'>DO NOT RUN THIS UNLESS YOU ARE SURE YOU WANT TO DELETE THE CLUSTER<br/> <b/>

```python
myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)['Clusters'][0]
prettyRedshiftProps(myClusterProps)
```

<div>
  <table border="1" class="dataframe">
    <thead>
     <tr style="text-align: right;">
       <th></th>
       <th>Key</th>
       <th>Value</th>
      </tr>
   </thead>
    <tbody>
      <tr>
      <th>0</th>
      <td>ClusterIdentifier</td>
      <td>dwhcluster</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NodeType</td>
      <td>dc2.large</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ClusterStatus</td>
      <td>deleting</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MasterUsername</td>
      <td>dwhuser</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DBName</td>
      <td>dwh</td>
    </tr>
    <tr>
        <th>5</th>
        <td>Endpoint</td>
        <td>{'Address': 'dwhcluster.c4m4dhrmsdov.us-west-2.redshift.amazonaws.com', 'Port': 5439}</td>
    </tr>
        <tr>
        <th>6</th>
        <td>VpcId</td>
        <td>vpc-9a53d7e2</td>
      </tr>
      <tr>
        <th>7</th>
        <td>NumberOfNodes</td>
        <td>4</td>
     </tr>
    </tbody>
  </table>
</div>

## Conclusion

The power of infrastructure-as-code is evident in the fact that we were able to launch a 4-node Redshift cluster, perform our analysis, and destroy all the resources, without once having to login to AWS console. This is the essense of cloud computing, wherein, you can spin the resources as-and-when you want, do whatever task you wish to do, and clean up the resources.
