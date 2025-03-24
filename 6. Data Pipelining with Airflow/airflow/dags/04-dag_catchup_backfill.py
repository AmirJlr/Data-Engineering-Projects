from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

default_args = {
    'owner' : 'AmiR',
    'retries' : 3,
    'retry_delay' : dt.timedelta(minutes=2)
}

with DAG(dag_id='04_catchup_backfill_v01', 
        default_args=default_args,
        start_date=dt.datetime(2025, 3, 1),
        schedule_interval='@daily',
        catchup=True
    ) as dag:

    task1 = BashOperator(task_id='first_task', bash_command='echo "This is a simple bash task"')