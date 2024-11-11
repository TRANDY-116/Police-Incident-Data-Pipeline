select
    incident_id,
    resolution,
    report_datetime,
    case
        when resolution = 'Open or Active' then 1
        else 0
    end as is_active,
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
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
    date_diff(day, cast(incident_datetime as date), cast(report_datetime as date)) as case_duration
from {{ source('police_data', 'police_2024') }}

