from airflow.decorators import dag, task
import datetime as dt


default_args = {
    'owner' : 'AmiR',
    'retries' : 3,
    'retry_delay' : dt.timedelta(minutes=2)
}

@dag(dag_id='03_taskflow_v01', 
    default_args=default_args, 
    start_date=dt.datetime(2025, 3, 24), 
    schedule_interval='@daily')
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'fist_name':'Amirrr',
            'last_name':'Jlr'
        }
    
    @task()
    def get_age():
        return 25
    
    @task()
    def greet(first_name, last_name, age):
        print(f'Hello, {first_name} {last_name} with {age} years old. Welcome to apache airflow!!!')
    
    name_dict = get_name()
    age = get_age()
    greet(name_dict['first_name'], name_dict['last_name'], age)

greet_dag = hello_world_etl()


