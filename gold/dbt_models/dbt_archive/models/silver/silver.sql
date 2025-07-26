{{ config(materialized='table') }}

SELECT
    time,
    systems.equipment_id AS equipment_id,
    users.my_status.status AS status
FROM {{ ref('bronze') }}
