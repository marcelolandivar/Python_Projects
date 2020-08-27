#!/usr/bin/env python
# coding: utf-8

# In[2]:


from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.exceptions import AirflowException
from datetime import datetime, timedelta


# In[3]:


default_args = {
    'owner': 'Marcelo',
    'depends_on_past' : False,
    'start_date': datetime(2020, 3, 3),
    #'end_date:datetime(),'
    'email':['marcelolandivar24@gmail.com'],
    'email_on_failure':True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    #'trigger_rule':'all_success'
}

dag = DAG('Pipeline',
         default_args=default_args,
         description='My pipeline',
         schedule_interval='0 * * * *',
         )

task1 = BashOperator(dag=dag,
                     task_id='dowload_files',
                     bash_command='python dowload_files_s3.py'
                    )

task2 = BashOperator(
    task_id='run_model',
    bash_command= 'python Model_training.py',
    dag=dag
)
    
    

task3 = BashOperator(dag=dag, 
                     task_id='update_db',
                     bash_command='python mysqlconnection.py'
                    )

task1 >> task2 >> task3
    

