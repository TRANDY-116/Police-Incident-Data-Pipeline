select distinct
    police_district,
    analysis_neighborhood,
    supervisor_district,
    latitude,
    longitude
from {{ source('police_data', 'police_2018') }}


