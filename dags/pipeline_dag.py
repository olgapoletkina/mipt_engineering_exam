from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

etl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'etl'))
sys.path.append(etl_path)

from etl.load_data import load_data
from etl.preprocess_data import preprocess_data, save_scaler
from etl.train_model import train_model, save_model
from etl.evaluate_model import evaluate_model, save_metrics
from etl.save_results import ensure_results_dir

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='breast_cancer_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for breast cancer model',
    schedule_interval='@daily', 
    catchup=False
)

def task_create_results_dir():
    ensure_results_dir()

def task_full_pipeline():
    X, y = load_data()
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(X, y)
    save_scaler(scaler)

    model = train_model(X_train_scaled, y_train)
    save_model(model)

    metrics = evaluate_model(model, X_test_scaled, y_test)
    save_metrics(metrics)
    print("Pipeline finished successfully!")

create_results_dir = PythonOperator(
    task_id='create_results_dir',
    python_callable=task_create_results_dir,
    dag=dag
)

full_pipeline = PythonOperator(
    task_id='full_pipeline',
    python_callable=task_full_pipeline,
    dag=dag
)

create_results_dir >> full_pipeline
