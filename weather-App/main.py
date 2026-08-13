import requests
print("Weather App ")
city = input("Enter city name: ")
url = "https://geocoding-api.open-meteo.com/v1/search"
params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    if "results" in data:
        location = data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }
        weather_response = requests.get(
            weather_url,
            params=weather_params
        )
        if weather_response.status_code == 200:
            weather = weather_response.json()
            current = weather["current"]
            print("\n=== Current Weather ===")
            print("City:", city_name)
            print("Temperature:", current["temperature_2m"], "°C")
            print("Humidity:", current["relative_humidity_2m"], "%")
            print("Wind Speed:", current["wind_speed_10m"], "km/h")
        else:
            print("Could not get weather data.")
    else:
        print("City not found.")
else:
    print("Could not connect to the weather service.")
