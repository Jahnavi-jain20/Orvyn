import requests
from config import WEATHER_API_KEY


def get_weather(city="Meerut"):

    url = (

        "https://api.openweathermap.org/data/2.5/weather"

        f"?q={city}"

        f"&appid={WEATHER_API_KEY}"

        "&units=metric"

    )

    try:

        response = requests.get(url)

        data = response.json()

        if data.get("cod") != 200:

            return f"Could not find weather for {city.title()}."

        temperature = data["main"]["temp"]

        feels_like = data["main"]["feels_like"]

        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        return (

            f"The weather in {city.title()} is "

            f"{description} with a temperature of "

            f"{temperature}°C. "

            f"It feels like {feels_like}°C "

            f"and the humidity is {humidity}%."

        )

    except Exception:

        return "Unable to fetch weather information."