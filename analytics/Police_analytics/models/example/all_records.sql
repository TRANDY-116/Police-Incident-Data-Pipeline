select * from {{ source('police_data', 'police_2018') }}
union all
select * from {{ source('police_data', 'police_2019') }}
union all
select * from {{ source('police_data', 'police_2020') }}
union all
select * from {{ source('police_data', 'police_2021') }}
union all
select * from {{ source('police_data', 'police_2022') }}
union all
select * from {{ source('police_data', 'police_2023') }}
union all
select * from {{ source('police_data', 'police_2024') }}
