SELECT *
FROM {{ ref('fct_hospital') }}
WHERE total_discharges < 0