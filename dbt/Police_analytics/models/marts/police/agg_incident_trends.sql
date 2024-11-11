with monthly_counts as (
    select
        incident_month,
        incident_category,
        count(*) as incident_count,
        incident_day_of_week,
        case 
            when extract(month from incident_datetime) in (6, 7, 8) then 'Summer'
            when extract(month from incident_datetime) in (12, 1, 2) then 'Winter'
            else 'Other' 
        end as season
    from {{ ref('stg_police_incidents') }}
    group by 1, 2, 4, incident_datetime
    order by 1, 2
)

select * from monthly_counts
