FROM apache/airflow:3.1.0

# Switch to root to install system packages first
USER root
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    less \
    && apt-get clean

# Switch back to airflow user for pip installs
USER airflow

# Copy and install Python requirements if they exist
COPY --chown=airflow:root requirements.txt* ./
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]