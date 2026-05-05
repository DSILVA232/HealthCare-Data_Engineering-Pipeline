USE DATABASE HEALTHCARE_DB;
USE ROLE engineer;
USE SCHEMA raw;
USE WAREHOUSE development;

-- test run to see if it works first, using validation mode 
COPY INTO hospital_data_raw
FROM @my_gcs_stage
FILE_FORMAT = (FORMAT_NAME = my_csv_format)
VALIDATION_MODE = RETURN_ERRORS;


-- if validation mode passes run this to copy into actual table 
COPY INTO hospital_data_raw
FROM @my_gcs_stage
FILE_FORMAT = (FORMAT_NAME = my_csv_format)

MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
ON_ERROR = 'ABORT_STATEMENT'

INCLUDE_METADATA = (
    ingestion_timestamp = METADATA$START_SCAN_TIME,
    source_file = METADATA$FILENAME
);