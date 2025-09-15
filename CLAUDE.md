# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django-based homicide tracking application for Charlotte with a React frontend. The project tracks homicide data and visualizes it using charts and maps. It's deployed to Azure and includes telemetry integration.

## Architecture

- **Backend**: Django 2.2.3 with Django REST Framework
- **Frontend**: React 16.9 with Ant Design components
- **Database**: SQLite (default) with MySQL configuration available
- **Bundling**: Webpack 4 with Babel transpilation
- **Visualization**: Altair charts for data analysis
- **Deployment**: Azure App Service with Application Insights telemetry

### Key Components

- **tracker/models.py**: Core data models (Homicide, Article, Historical)
- **tracker/views.py**: API endpoints and chart generation using Altair
- **assets/src/js/**: React frontend components
- **homicide/settings.py**: Main Django configuration with Azure integration

## Development Commands

### Python/Django Commands
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run Django development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
pytest
# or
python manage.py test
```

### Frontend Commands
```bash
# Install JavaScript dependencies
npm install

# Build frontend assets (development)
npm run build

# Watch mode for development
npm run watch

# Run React tests
npm test
```

## Database Configuration

- Default: SQLite (`db.sqlite3`)
- Alternative: MySQL (see `settings.mysql.py`)
- Use `devsettings.py` for development-specific settings

## Data Models

- **Homicide**: Main model with victim/killer demographics, location, motive, means
- **Article**: News articles related to homicides with sentiment analysis
- **Historical**: Historical homicide data by year

## Chart Endpoints

The application provides various chart endpoints in `tracker/views.py`:
- `/chart_obj/` - Age/Gender visualization
- `/chart_cod/` - Cause of death analysis
- `/chart_heat/` - Age vs Ethnicity heatmap
- `/chart_tod/` - Time of day analysis
- `/chart_regression/` - Polynomial regression predictions

## Static Files

- Frontend assets built to `assets/dist/`
- Webpack stats tracked in `webpack-stats.json`
- Static files served from `assets/` directory

## Azure Deployment

- Application Insights integration with instrumentation key
- Static file deployment script: `copystatic.sh`
- SSL redirect disabled for Azure compatibility