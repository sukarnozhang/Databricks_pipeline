{{ config(materialized='table') }}

SELECT *
FROM bronze_table
