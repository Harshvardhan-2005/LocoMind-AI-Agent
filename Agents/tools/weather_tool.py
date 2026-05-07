import requests

from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """
    Get current weather information for a city.
    """

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        desc = current["weatherDesc"][0]["value"]

        return (
            f"Weather in {city}:\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {desc}\n"
            f"Humidity: {humidity}%"
        )

    except Exception as e:

        return f"Weather tool error: {str(e)}"