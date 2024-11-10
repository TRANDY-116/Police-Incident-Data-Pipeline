select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2018') }}
\
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2019') }}

union all

select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2020') }}

union all

select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2021') }}

union all

select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2022') }}

union all

select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2023') }}

union all

select
    incident_id,
    incident_number,
    incident_day_of_week,
    CAST(incident_datetime AS timestamp) AS incident_datetime,
    incident_category,
    incident_subcategory,
    incident_description,
    report_type_code,
    report_type_description,
    police_district,
    latitude,
    longitude,
    _intersection
from {{ source('police_data', 'police_2024') }}

