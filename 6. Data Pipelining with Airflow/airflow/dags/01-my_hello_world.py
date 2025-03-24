from airflow import DAG
# with DAG() as dag:
#     pass

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import datetime as dt

def print_world():
    print('World from Python!')


default_args = {
    'owner' : 'amir',
    'start_date' : dt.datetime(2025, 3, 22),
    'retries' : 1,
    'retry_delay' : dt.timedelta(minutes=2)
}

with DAG(dag_id='01_hello_world', default_args=default_args, schedule_interval='0 * * * *') as dag:

    print_hello = BashOperator(task_id='print_hello', bash_command='echo "Hello from Bash!" ')

    sleep = BashOperator(task_id='sleep', bash_command='sleep 5')

    print_world = PythonOperator(task_id='print_world', python_callable=print_world)


print_hello >> sleep >> print_world