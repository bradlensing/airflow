## Airflow Code and Notes

Assuming airflow is installed on computer or docker container

### Running Airflow Locally

In 2 seperate terminal windows run following commands

- $ airflow webserver --port 8080
- $ airflow scheduler

In browser visit localhost:8080

### Running Airflow through Docker

[Docker yaml file set to run in local mode](./docker-compose-airflow.yaml)

1. In airflow folder run
   - docker-compose -f docker-compose-airflow.yaml up -d
1. In VS Code Docker Tools
   - Double click on the webserver container and Attach Shell
   - May have to restart container
1. To stop running containers
   - docker-compose-airflow down

### DAGs

- [Demo Dag](./1.1-DemoDAG.py)
- [Monthly Interval Dag](./1.2-DemoMonthlyDAG.py)
- [Tasks and Dependencies](./1.3-DemoTaskAndDependenciesDAG.py)
- [Using Connections, Variables and Hooks to connect an S3 bucket and log out all the sub directories](./ConnectionsAndHooksAWSDAG.py)
- [Creating Users Table - Fetching Data - Saving to CSV - Populating to DB Dag](/CompleteIntro/0.1-CreatingTableDAG.py)
- [S3 to Redshift DAG](./S3ToRedshiftDAG.py)
  - [Create Redshift Cluster Notebook (.ipynb file)](./S3ToRedshiftCreation.ipynb)
  - [Documentation on Pipeline Creation ](./S3ToRedshift.md)
