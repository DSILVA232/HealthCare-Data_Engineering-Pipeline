# Infrastructure Setup

> **Read this file top to bottom and complete each section in order before moving to the next.**
> Most project folders contain their own README with component-specific details. This file covers infrastructure only.

---

## Prerequisites

Before starting, confirm you have:

- Python 3.11+
- Docker Desktop installed and running
- A Google Cloud account
- A Snowflake account (free trial is fine)
- Git

---

## 1. Clone and Install

```bash
git clone <repo-url>
cd healthcare
```

**Create and activate a virtual environment:**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:
```bash
python -m venv venv
source venv/bin/activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Verify:**
```bash
python --version   # should be 3.11+
pip list           # confirm packages installed
```

---

## 2. Environment Variables

Create a `.env` file in the project root by copying the example:

```bash
cp .env.example .env
```

Fill in all values before proceeding. The `.env` file is gitignored and never committed.

Key variables:

```env
# GCP
GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/health_care_project/keys/gx-key.json
GCP_BUCKET_NAME=landing-zone-1

# Snowflake
SNOWFLAKE_ACCOUNT=your-account
SNOWFLAKE_USER=your-user
SNOWFLAKE_PASSWORD=your-password
SNOWFLAKE_DATABASE=HEALTHCARE_DB
SNOWFLAKE_SCHEMA=RAW
SNOWFLAKE_WAREHOUSE=DEVELOPMENT
SNOWFLAKE_ROLE=ENGINEER

# Airflow Snowflake connection — replace all placeholders with your real values
AIRFLOW_CONN_SNOWFLAKE_DEFAULT=snowflake://YOUR_USER:YOUR_PASSWORD@YOUR_ACCOUNT/HEALTHCARE_DB/RAW?warehouse=DEVELOPMENT&role=ENGINEER
```

> **Note:** `AIRFLOW_CONN_SNOWFLAKE_DEFAULT` must use your actual credentials, not the variable names above it.

---

## 3. Google Cloud Platform

> These steps assume an existing GCP account with billing enabled.

**Install the Google Cloud CLI:**
https://cloud.google.com/sdk/docs/install

**Run the GCP setup script:**

Open `google_cloud/setup_gcp.sh` and update the required variables at the top of the file before running.

```bash
bash google_cloud/setup_gcp.sh
```

This script handles:
- GCP authentication
- Project configuration
- Service account creation
- IAM role assignment
- Service account key generation

**Create the GCS bucket:**

Create a bucket named `landing-zone-1`. Using this name means no additional configuration changes are needed elsewhere in the project.

**Verify:**
```bash
gcloud auth list                        # confirm active account
gcloud storage buckets list             # confirm bucket exists
```

---

## 4. Snowflake

> These steps assume an existing Snowflake account.

Run the SQL setup scripts in the following order. Each script must complete without errors before running the next.

| Order | File | Purpose |
|-------|------|---------|
| 1 | `SQL/bootstrap.sql` | Creates databases, schemas, roles, warehouse |
| 2 | `SQL/landing_zone_setup.sql` | Configures RAW schema and tables |
| 3 | `SQL/storage_integration.sql` | Links Snowflake to your GCS bucket |

Reference: https://docs.snowflake.com/en/user-guide/data-load-gcs-config

**Verify:**

After running all three scripts, confirm in Snowflake:
- Database `HEALTHCARE_DB` exists
- Schemas `RAW`, `STAGING`, `MARTS` exist
- Storage integration is active

---

## 5. Great Expectations

GX resources are preconfigured. To initialise them:

```bash
python gx_context/gx_setup.py
```

This creates:
- Datasource
- Data assets
- Expectation suite
- Checkpoint

**Verify:**
```bash
python -c "import great_expectations as gx; print(gx.__version__)"
```

---

## 6. Docker and Airflow

Start all containers from the project root:

```bash
docker compose up --build
```

First startup will take several minutes while images are pulled and built.

**Once running, configure the Snowflake connection in the Airflow UI:**

1. Open `http://localhost:8080`
2. Go to **Admin → Connections**
3. Add a new connection with connection ID `snowflake_default`
4. Enter your Snowflake credentials matching your `.env` values

**Verify:**
```bash
docker compose ps        # all containers should show status: running
```

Then open `http://localhost:8080` and confirm the Airflow UI loads.

---

## 7. Trigger the Pipeline

Once all steps above are complete and verified:

1. Open the Airflow UI at `http://localhost:8080`
2. Locate the pipeline DAG
3. Toggle it on and trigger a manual run
4. Monitor task logs for any failures

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Docker containers not starting | Docker Desktop not running | Start Docker Desktop first |
| GCP auth errors | Key file path wrong in `.env` | Check `GOOGLE_APPLICATION_CREDENTIALS` path |
| Snowflake connection failing | Account identifier format wrong | Check format: `xy12345.us-east-1` |
| GX setup fails | Dependencies not installed | Re-run `pip install -r requirements.txt` |
| Airflow UI not loading | Containers still initialising | Wait 2-3 minutes and retry |
