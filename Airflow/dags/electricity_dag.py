from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():

    df = extract_data()
    df = transform_data(df)
    load_data(df)


with DAG(
    dag_id="electricity_etl_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline
    )