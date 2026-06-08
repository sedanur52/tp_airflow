from datetime import datetime
import sys
import os

# 1. Chemin absolu dans Docker pour forcer la détection du dossier src
sys.path.append("/opt/airflow/src")
sys.path.append("/opt/airflow/src/data_job")

# 2. Injection des variables d'environnement pour config.py
os.environ["INPUT_PATH"] = "/opt/airflow/input.xlsx"
os.environ["OUTPUT_PATH"] = "/opt/airflow/sales_clean.csv"
os.environ["MIN_AMOUNT"] = "0"

# 3. Imports Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

# 4. Import direct de ta fonction depuis le dossier maintenant reconnu
from main import run

with DAG(
    dag_id="tp2_data_job",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="TP : job data orchestré",
) as dag:

    run_job = PythonOperator(
        task_id="run_data_job",
        python_callable=run
    )