
with data as (
    select
        row_id,
        incident_id,
        cnn
    from {{ ref('all_records') }}
)

-- Check if any integer field exceeds its allowed range
select *
from data
where 
    row_id > 2147483647 or row_id < -2147483648
    or incident_id > 2147483647 or incident_id < -2147483648
    or cnn > 2147483647 or cnn < -2147483648
    