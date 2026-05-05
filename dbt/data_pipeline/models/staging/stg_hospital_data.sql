SELECT
    Rndrng_Prvdr_CCN AS provider_ccn,
    Rndrng_Prvdr_Org_Name AS provider_name,
    TRIM(Rndrng_Prvdr_City) AS city,
    TRIM(Rndrng_Prvdr_St) AS state,
    Rndrng_Prvdr_State_FIPS AS state_Fips,
    Rndrng_Prvdr_Zip5 AS zip_code,
    Rndrng_Prvdr_State_Abrvtn AS state_abbr,
    Rndrng_Prvdr_RUCA AS ruca,
    Rndrng_Prvdr_RUCA_DESC AS ruca_desc,
    DRG_Cd AS drg_code,
    TRIM(DRG_Desc) AS drg_description,
    CAST(Tot_Dschrgs AS INT) AS total_discharges,
    CAST(Avg_Submtd_Cvrd_Chrg AS FLOAT) AS avg_submitted_charge,
    CAST(Avg_Tot_Pymt_Amt AS FLOAT) AS avg_total_payment,
    CAST(Avg_Mdcr_Pymt_Amt AS FLOAT) AS avg_medicare_payment,
    ingestion_timestamp,
    source_file

FROM {{ source('healthcare', 'HOSPITAL_DATA_RAW') }}