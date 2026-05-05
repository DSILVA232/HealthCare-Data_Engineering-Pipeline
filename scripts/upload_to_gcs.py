from google.cloud import storage
from pathlib import Path
import os 

base_dir = "/opt/airflow/health_care_project"

def upload_to_gcs():
    bucket_name = "landing-zone-1"
    file_path = os.path.join(base_dir,"data/raw/Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv")
    destination_blob = "raw/data/Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv"
    creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    client = storage.Client.from_service_account_json(creds)
    bucket = client.bucket(bucket_name)

    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(file_path)

    print(f"Uploaded {file_path} → {bucket_name}/{destination_blob}")