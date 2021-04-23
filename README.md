## Airflow Code and Notes

Assuming airflow is installed on computer or docker container

### Running Airflow Locally

1. airflow webserver --port 8080
1. airflow scheduler
1. In browser localhost:8080

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
- [Demo Monthly Dag](./1.2-DemoMonthlyDAG.py)
- [Demo Task and Dependencies](./1.3-DemoTaskAndDependenciesDAG.py)
- [Creating Users Table - Fetching Data - Saving to CSV - Populating to DB Dag](./CompleteHandsOnIntroduction/0.1-CreatingTableDAG.py)
