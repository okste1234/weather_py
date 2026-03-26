# Weather script via API (HTTP, Python)

## Get data from Open-Meteo (no API key needed). Parse the JSON, output temperature and precipitation in a readable format. Handle 404 and timeout

import os
import urllib.request
import json
import sys
from dotenv import load_dotenv
load_dotenv()


API_URL = os.getenv("WEATHER_API_URL", "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true")

def fetch_weather():
    try:
        with urllib.request.urlopen(API_URL, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())

                current_weather = data.get("current_weather", {})
                temperature = current_weather.get("temperature")
                windspeed = current_weather.get("windspeed")

                precipitation = data.get("hourly", {}).get("precipitation", [])

                print(f"🌡 Temperature: {temperature}°C")
                print(f"💨 Wind Speed: {windspeed} km/h")
                print(f"🌧 Precipitation: {precipitation[0] if precipitation else 0} mm")

            else:
                print(f"Error: Received status code {response.status}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Error: Data not found (404)")
        else:
            print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_weather()

