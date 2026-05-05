#!/bin/bash
## Prerequisites

Before running the setup script, ensure you have:

1. Installed Google Cloud CLI
   https://cloud.google.com/sdk/docs/install

2. Logged in to your Google account:
   gcloud auth login

3. Set your active project:
   gcloud config set project YOUR_PROJECT_ID

4. (Optional) Verify setup:
   gcloud auth list

IF yes to all the above proceed below


PROJECT_ID="your-project-id"
SA_NAME="gx-pipeline-sa"
KEY_PATH="./keys/gx-key.json"


gcloud iam service-accounts create $SA_NAME \
  --project=$PROJECT_ID \
  --display-name="GX Pipeline Service Account"


gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"


mkdir -p keys
gcloud iam service-accounts keys create $KEY_PATH \
  --iam-account="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

echo "Key saved to $KEY_PATH"