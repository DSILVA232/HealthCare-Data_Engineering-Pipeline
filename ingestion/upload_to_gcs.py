from google.cloud import storage

bucket_name = "landing-zone-1"
file_path = "../data/raw/Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv"
destination_blob = "raw/data/Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv"

def upload_blob():
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(file_path)

    print(f"Uploaded {file_path} : {bucket_name}/{destination_blob}")

if __name__ == "__main__":
    upload_blob()