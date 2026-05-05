import datetime
import os 
from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from gx_context.my_gx_script import run_gx_validation
from scripts.upload_to_gcs import upload_to_gcs
from airflow.utils.email import send_email


def email_alert(context):
    task_instance = context.get("task_instance")
    dag_id = context.get("dag").dag_id

    send_email(
        to="you@email.com", # set you're email for alerts
        subject=f"Airflow Task Failed: {dag_id}",
        html_content=f"""
        <h3>Task Failed</h3>
        <p><b>DAG:</b> {dag_id}</p>
        <p><b>Task:</b> {task_instance.task_id}</p>
        <p><b>Execution Time:</b> {context.get("ts")}</p>
        <p><b>Log:</b> {task_instance.log_url}</p>
        """
    )

default_args = {
    "on_failure_callback": email_alert
}

with DAG(
    dag_id="healthcare_project_dag",
    start_date=datetime.datetime(2026, 5, 1),
    schedule=None,
    catchup=False,
    default_args=default_args
) as dag:

    dbt_run = BashOperator(
        task_id="run_dbt",
        bash_command="cd /opt/airflow/health_care_project/dbt/data_pipeline && dbt run"
    )

    load_data = SQLExecuteQueryOperator(
        task_id="load_data",
        conn_id="snowflake_default",
        sql="SQL/Data_Loading/ingestion.sql"
    )

    gx_task = PythonOperator(
        task_id="run_gx",
        python_callable=run_gx_validation,
    )

    upload_to_gcs_task = PythonOperator(
        task_id="upload_to_gcs",
        python_callable=upload_to_gcs
    )

    upload_to_gcs_task >> gx_task >> load_data >> dbt_run