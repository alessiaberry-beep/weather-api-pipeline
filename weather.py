import requests
import json
import time
import pandas as pd

API_KEY = "0af6b211e6584c4bb9a175127261304"

api_url = "https://api.weatherapi.com/v1/forecast.json"  # API endpoint for forecast

zip_codes = [
    "90045",  # Los Angeles, CA
    "10001",  # New York, NY
    "60601",  # Chicago, IL
    "98101",  # Seattle, WA
    "33101",  # Miami, FL
    "85001",  # Phoenix, AZ
    "19101",  # Philadelphia, PA
    "78201",  # San Antonio, TX
    "92101",  # San Diego, CA
    "75201",  # Dallas, TX
    "95101",  # San Jose, CA
    "78701",  # Austin, TX
    "32099",  # Jacksonville, FL
    "76101",  # Fort Worth, TX
    "43085",  # Columbus, OH
    "46201",  # Indianapolis, IN
    "28201",  # Charlotte, NC
    "94102",  # San Francisco, CA
    "80201",  # Denver, CO
    "02101",  # Boston, MA
]

results = []

for zip_code in zip_codes:
    # Parameters for the API request
    params = {
        "key": API_KEY,
        "q": zip_code,
        "days": 7
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    city = data["location"]["name"]
    region = data["location"]["region"]

    print(f"\n{city}, {region} - 7 Day Forecast:")

    for day in data["forecast"]["forecastday"]:
        result = {
            "zip_code": zip_code,
            "city": city,
            "region": region,
            "date": day["date"],
            "max_temp_f": day["day"]["maxtemp_f"],
            "min_temp_f": day["day"]["mintemp_f"],
            "condition": day["day"]["condition"]["text"],
        }
        results.append(result)

        print(f"  {result['date']}: {result['min_temp_f']}°F - {result['max_temp_f']}°F, {result['condition']}")

    time.sleep(1)  # 1-second delay between API calls

df = pd.DataFrame(results)

print("\n" + "="*80)
print("7-Day Forecast Data")
print("="*80)
print(df.to_string(index=False))

rows, cols = df.shape
print(f"\nTable dimensions: {rows} rows x {cols} columns")

df.to_csv("weather_data.csv", index=False)
print("Saved to weather_data.csv")

