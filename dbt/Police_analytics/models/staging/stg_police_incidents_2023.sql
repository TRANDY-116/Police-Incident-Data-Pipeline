with raw_data as (
    select
        incident_datetime,
        incident_category,
        incident_day_of_week,
        incident_year,
        extract(month from incident_datetime) as incident_month,
        extract(day from incident_datetime) as incident_day,
        case 
            when filed_online = 1 then true
            else false
        end as filed_online
    from {{ source('police_data_st', 'police_2023') }}
)

select * from raw_data

