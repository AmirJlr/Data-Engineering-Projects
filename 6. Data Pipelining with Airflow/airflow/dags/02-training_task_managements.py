from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import datetime as dt



default_args = {
    'owner' : 'AmiR',
    'start_date' : dt.datetime(2025, 3, 23),
    'retries' : 3,
    'retry_delay' : dt.timedelta(minutes=2)
}


def consumer(age, ti):
    name = ti.xcom_pull(task_ids='info_producer', key='name')
    jobs = ti.xcom_pull(task_ids='info_producer', key='jobs')

    print(f"Hello {name} with {age} years old, with {jobs} jobs")


def producer(ti):
    ti.xcom_push(key='name', value='Amirrr')
    ti.xcom_push(key='jobs', value=['Data Eng', 'Teacher'])

    

with DAG(
    dag_id='02_manage_tasks_v01',
    description='training managements tasks as upstream and downstream',
    default_args=default_args,
    schedule_interval='@daily'
    ) as dag:
    
    """
    Manage Task Dependencies with defferent methods and then share parameters between task using 'xcom'
    """
    
    task1 = BashOperator(task_id='first_task', bash_command='echo "Hey this is task 1 and upstream for all tasks"')
    task2 = BashOperator(task_id='second_task', bash_command='echo "Hey this is task 2 and executes same time as task 3"')
    task3 = BashOperator(task_id='third_task', bash_command='echo "Hey this is task 3 and executes same time as task 2"')

    task4 = PythonOperator(task_id='info_consumer', python_callable=consumer, op_kwargs={'age':25})
    task5 = PythonOperator(task_id='info_producer', python_callable=producer)

    

    ## Task Dependencies method 1:
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    ## Task Dependencies method 2:
    # task1 >> task2
    # task1 >> task3

    ## Task Dependencies method3:
    task1 >> [task2, task3]
    task2 >> task5 >> task4