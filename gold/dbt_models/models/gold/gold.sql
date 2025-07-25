{{ config(materialized='table') }}

SELECT
    status,
    COUNT(*) AS record_count
FROM {{ ref('silver') }}
GROUP BY status
