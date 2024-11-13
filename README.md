# Police Incident Data Pipeline

This project builds a data pipeline to ingest, transform, and analyze police incident data. It utilizes Mage AI for orchestrating API data ingestion, dbt for data transformation, Docker to manage PostgreSQL and PgAdmin services, and Jupyter Notebook for exploratory data analysis and visualization.

## Project Overview

1. **Data Ingestion**:
   - **API Data**: Police incident data is fetched from an external API.
   - **Orchestration**: Mage AI manages the data ingestion pipeline, ensuring smooth extraction and loading into the database.

2. **Database**:
   - **PostgreSQL**: Data is stored in a structured relational database.
   - **PgAdmin**: A user-friendly interface for managing the database.
   - **Docker**: Both PostgreSQL and PgAdmin are set up within Docker containers for easy configuration and management.

3. **Data Transformation**:
   - **dbt (Data Build Tool)**: Transforms raw data into meaningful views and aggregates for analysis, facilitating modular and scalable SQL transformations.

4. **Data Models**:
   - **Fact and Dimension Tables**:
     - `fact_incidents`: Fact table containing incident records.
     - `dim_resolution`, `dim_location`, `dim_date`, `dim_incident_type`: Dimension tables for additional information on resolutions, locations, dates, and incident types.
   - **Aggregated Views**:
     - `agg_incident_trends`, `agg_incident_trends_2023`: Aggregated tables for analyzing trends in incidents.
     - `all_records`: Combines all data records for broader analysis.
   - **Staging Tables**:
     - `stg_police_incidents`, `stg_police_incidents_2023`: Staging tables holding intermediary data during transformation.

5. **Data Analysis**:
   - **Jupyter Notebook**: Used for exploratory data analysis, visualization, and forecasting trends in incidents.

## Key Technologies

- **Mage AI**: Manages data orchestration tasks, automating the extraction of API data.
- **Docker**: Used to containerize PostgreSQL and PgAdmin, streamlining setup and dependencies.
- **PostgreSQL**: A reliable database system for storing and querying incident data.
- **dbt**: Facilitates SQL-based data transformation, enabling modularized views and data processing.
- **Jupyter Notebook**: Provides an interactive environment for analyzing and visualizing trends, conducting time-series analysis, and identifying patterns in incident data.

## Getting Started

1. **Set Up Docker**: Start PostgreSQL and PgAdmin containers using the project's `docker-compose.yml` file.
2. **Run Mage AI Pipeline**: Use Mage AI to fetch and load data into the PostgreSQL database.
3. **Execute dbt Models**: Run dbt to transform data and create necessary tables and views.
4. **Analysis with Jupyter Notebook**: Open Jupyter Notebook to perform exploratory data analysis and visualize trends.

## Future Improvements

- Implement automated testing for data quality checks.
- Integrate with BI tools to visualize incident trends and insights!