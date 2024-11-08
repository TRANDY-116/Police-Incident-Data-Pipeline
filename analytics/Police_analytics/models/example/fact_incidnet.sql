select
    incident_id,
    incident_number,
    incident_datetime,
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
