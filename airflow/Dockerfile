FROM apache/airflow:3.0.5
USER root

ENV AIRFLOW_HOME=/opt/airflow
RUN apt-get update -qq && apt-get install vim -qqq
# git gcc g++ -qqq

COPY requirements.txt .
USER $AIRFLOW_UID
RUN pip install --no-cache-dir -r requirements.txt

# Ref: https://airflow.apache.org/docs/docker-stack/recipes.html

# SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

WORKDIR $AIRFLOW_HOME

# COPY scripts scripts
# RUN chmod +x scripts

USER $AIRFLOW_UID