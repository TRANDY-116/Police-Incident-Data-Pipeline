with dates as (
    select generate_series(
        '2015-01-01'::date, '2025-12-31'::date, interval '1 day'
    ) as date
)

select
    date as full_date,
    extract(year from date) as year,
    extract(month from date) as month,
    extract(day from date) as day,
    extract(dow from date) as day_of_week,
    extract(quarter from date) as quarter
from dates
