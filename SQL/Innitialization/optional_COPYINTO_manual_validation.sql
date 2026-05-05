-- Optional validation script for manual testing of GCS → Snowflake ingestion
--
-- This script is NOT required for the automated pipeline.
-- It is intended as a pre-flight check to ensure:
-- 1. GCS connectivity is working
-- 2. File format is compatible with Snowflake
-- 3. Data can be parsed without errors
--
-- IMPORTANT:
-- This script does NOT load data into the target table.
-- It only performs a validation scan using Snowflake's COPY INTO validation mode.

COPY INTO HEALTHCARE_DB.RAW.HOSPITAL_DATA_RAW
FROM @my_gcs_stage
FILE_FORMAT = (FORMAT_NAME = my_csv_format)
VALIDATION_MODE = RETURN_ERRORS;