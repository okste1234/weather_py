# Weather Py

A simple Python script to fetch and display current weather data from the Open-Meteo API. No API key required.

## Features

- Uses `urllib.request` for HTTP calls
- Supports environment-variable-driven API URL via `.env`
- Parses JSON response and prints:
  - Temperature (°C)
  - Wind speed (km/h)
  - Precipitation (first available hourly value)
- Handles:
  - HTTP 404 errors
  - Timeout and URL errors
  - Unexpected exceptions

## Requirements

- Python 3.8+
- `python-dotenv`

## Setup

1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install python-dotenv
```

3. Create `.env` in project root (example included):

```ini
WEATHER_API_URL="https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true&hourly=precipitation"
```

4. Verify `.gitignore` includes `.env` (done)

## Usage

```bash
python3 weather.py
```

## Notes

- The URL defaults to New York City coordinates if `WEATHER_API_URL` is not set.
- You can customize `WEATHER_API_URL` to any valid `open-meteo.com` endpoint.
