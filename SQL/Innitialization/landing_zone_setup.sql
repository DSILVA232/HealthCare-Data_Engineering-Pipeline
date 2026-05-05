USE DATABASE HEALTHCARE_DB;
USE ROLE engineer;
USE SCHEMA raw;
USE WAREHOUSE development;


--SANITY CHECK CURRENT USER
SELECT CURRENT_ROLE();

-- file format
CREATE OR REPLACE FILE FORMAT my_csv_format
TYPE = CSV
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
SKIP_HEADER = 1
NULL_IF = ('', 'NULL', 'null','NAN','nan')
TRIM_SPACE = TRUE;

-- stage, this will be saved under : RAW-STAGES-MY_GCS_STAGE
CREATE OR REPLACE STAGE my_gcs_stage
URL = 'gcs://landing-zone-1'
STORAGE_INTEGRATION = gcp_integration
FILE_FORMAT = my_csv_format;

-- raw table
CREATE OR REPLACE TABLE hospital_data_raw (
    Rndrng_Prvdr_CCN INT,
    Rndrng_Prvdr_Org_Name VARCHAR,
    Rndrng_Prvdr_City VARCHAR,
    Rndrng_Prvdr_St VARCHAR,
    Rndrng_Prvdr_State_FIPS INT,
    Rndrng_Prvdr_Zip5 INT,
    Rndrng_Prvdr_State_Abrvtn VARCHAR,
    Rndrng_Prvdr_RUCA FLOAT,
    Rndrng_Prvdr_RUCA_Desc VARCHAR,
    DRG_Cd INT,
    DRG_Desc VARCHAR,
    Tot_Dschrgs INT,
    Avg_Submtd_Cvrd_Chrg FLOAT,
    Avg_Tot_Pymt_Amt FLOAT,
    Avg_Mdcr_Pymt_Amt FLOAT,
    ingestion_date DATE,
    ingestion_timestamp TIMESTAMP,
    source_file VARCHAR
);

-- create validation table for data ingestion usage 
CREATE OR REPLACE TABLE validation_test_hospital_data_raw (
    Rndrng_Prvdr_CCN INT,
    Rndrng_Prvdr_Org_Name VARCHAR,
    Rndrng_Prvdr_City VARCHAR,
    Rndrng_Prvdr_St VARCHAR,
    Rndrng_Prvdr_State_FIPS INT,
    Rndrng_Prvdr_Zip5 INT,
    Rndrng_Prvdr_State_Abrvtn VARCHAR,
    Rndrng_Prvdr_RUCA FLOAT,
    Rndrng_Prvdr_RUCA_Desc VARCHAR,
    DRG_Cd INT,
    DRG_Desc VARCHAR,
    Tot_Dschrgs INT,
    Avg_Submtd_Cvrd_Chrg FLOAT,
    Avg_Tot_Pymt_Amt FLOAT,
    Avg_Mdcr_Pymt_Amt FLOAT
);