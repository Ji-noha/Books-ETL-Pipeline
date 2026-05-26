# Books ETL Pipeline
## Overview

This project is a containerized ETL pipeline designed to collect, transform, and store book data from external APIs.

The system automates data extraction, performs cleaning and preprocessing using Python and Pandas, stores the processed data in PostgreSQL, and visualizes insights through Metabase dashboards.

The project was built to practice data engineering concepts such as ETL workflows, containerization, database integration, and analytics visualization.

## Architecture
API Source → Python ETL Script → Data Cleaning (Pandas) → PostgreSQL → Metabase Dashboard

### Components:
- Python ETL scripts for extraction and transformation
- PostgreSQL database running in Docker
- Docker Compose orchestration
- Metabase for dashboard visualization

  ## Features

- Automated extraction of book data from APIs
- Data cleaning and preprocessing using Pandas
- PostgreSQL data storage
- Containerized infrastructure with Docker Compose
- Interactive dashboards with Metabase
- Modular ETL workflow structure

  ## Tech Stack

### Languages
- Python
- SQL

### Data Processing
- Pandas

### Database
- PostgreSQL

### Infrastructure
- Docker
- Docker Compose

### Visualization
- Metabase

## Installation

### Clone repository

```bash
git clone https://github.com/Ji-noha/Books-ETL-Pipeline
```
cd books-etl-pipeline

## Run ETL pipeline

docker compose up -d
python script.py

## Access PostgreSQL:
### Default PostgreSQL port: 
localhost:5432

### Open Metabase dashboard: 
http://localhost:3001


