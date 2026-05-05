SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['drg_code'])}} AS drg_key,
    drg_code,
    drg_description

FROM {{ref('stg_hospital_data')}}
