SELECT 
    dp.provider_key,
    d.drg_key,

    f.total_discharges,
    f.avg_submitted_charge,
    f.avg_total_payment,
    f.avg_medicare_payment,
    f.ingestion_timestamp

FROM  {{ ref('stg_hospital_data') }} as f

JOIN {{ ref('dim_provider') }} as dp
    ON f.provider_ccn = dp.provider_ccn

JOIN {{ ref('dim_drg') }} as d
    ON f.drg_code =  d.drg_code