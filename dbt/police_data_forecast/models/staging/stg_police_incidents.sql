-- models/staging/stg_police_incidents.sql
with raw_data as (
    select
        incident_datetime,
        incident_category,
        incident_day_of_week,
        extract(year from incident_datetime) as incident_year,
        extract(month from incident_datetime) as incident_month,
        extract(day from incident_datetime) as incident_day,
        filed_online::boolean as filed_online
    from {{ source('raw', 'police_incidents') }}
)

select * from raw_data
