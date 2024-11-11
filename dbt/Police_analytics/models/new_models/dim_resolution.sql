select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2018') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2019') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2020') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2021') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2022') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2023') }}

union all

select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    (report_datetime::date - incident_datetime::date) as case_duration
from {{ source('police_data', 'police_2024') }}
