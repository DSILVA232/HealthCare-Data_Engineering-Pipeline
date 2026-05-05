SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['provider_ccn']) }} AS provider_key,
    provider_ccn,
    provider_name,
    city,
    state,
    state_fips,
    zip_code,
    state_abbr,
    ruca,
    ruca_desc
FROM {{ ref('stg_hospital_data') }}