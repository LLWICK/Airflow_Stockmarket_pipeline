from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from stockMarket_etl import run_stockMarket_ETL

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='stockMarket_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    description='stock Market IBM ETL',
) as dag:

    run_etl = PythonOperator(
        task_id='complete_stockMarket_etl',
        python_callable=run_stockMarket_ETL,
    )
