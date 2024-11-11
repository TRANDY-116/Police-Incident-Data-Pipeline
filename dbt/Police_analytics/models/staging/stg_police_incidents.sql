with raw_data as (
    select
        incident_datetime,
        incident_category,
        incident_day_of_week,
        incident_year,
        extract(month from incident_datetime) as incident_month,
        extract(day from incident_datetime) as incident_day,
        filed_online::boolean as filed_online
    from {{ source('police_data', 'all_records') }}
)

select * from raw_data