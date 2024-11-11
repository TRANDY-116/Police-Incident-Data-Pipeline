with monthly_counts as (
    select
        date_trunc('month', incident_datetime) as incident_month,
        incident_category,
        count(*) as incident_count
    from {{ ref('stg_police_incidents') }}
    group by 1, 2
    order by 1, 2
)

select * from monthly_counts