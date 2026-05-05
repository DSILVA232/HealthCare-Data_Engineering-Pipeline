SELECT *
FROM {{ ref('fct_hospital') }}
WHERE avg_total_payment < 0