"""
Cron Expression is a string representing a set of times,
using 5 space-separated fields normally as a schedule to execute something at a specific time.

=> (minute hour day(month) month day(week))"

Also airflow has some preset schedule intervals :
none : Done schedule, use for exclusivly "txternal triggered" DAGs
@once : Run once and only once
@hourly : Run once an hour at the beginning of the hour | (0 * * * *)
@daily : Run once a day at midnight | (0 0 * * *)
@weekly : Run once a week at midnight on Sunday morning |  (0 0 * * 0)
@monthly : Run once a month at midnight of the first day of the month | (0 0 1 * *)
@yearly : Run once a year at midnight of January 1 | (0 0 1 1 *)

Custom cron expression: https://crontab.guru/
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

default_args ={
    'owner':'AmiR',
    'retries':1,
    'retry_delay':dt.timedelta(minutes=2)
}
with DAG(dag_id='05_expression_with_cron_v01', 
        default_args=default_args,
        start_date=dt.datetime(2025, 3, 15),
        schedule_interval='0 0 * * Sun,Wed') as dag:
    
    task1 = BashOperator(task_id='cron_task', bash_command='echo "This is an expression with cron"')
