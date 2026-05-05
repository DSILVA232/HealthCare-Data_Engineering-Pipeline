-- May need to RUN queries 1 at a time 

USE ROLE ACCOUNTADMIN;

CREATE SCHEMA IF NOT EXISTS HEALTHCARE_DB.gcp_staging;

CREATE STORAGE INTEGRATION gcp_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'GCS'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('gcs://landing-zone-1');


-- check the description/"status" of storage integration created above
DESC STORAGE INTEGRATION gcp_integration;

-- returns service account under column PRINCIPAL from previous query, that is needed to set up bucket permissions in gcp 
SELECT "property", "property_value" AS principal 
FROM TABLE(result_scan(last_query_id()))
WHERE "property" = 'STORAGE_GCP_SERVICE_ACCOUNT';