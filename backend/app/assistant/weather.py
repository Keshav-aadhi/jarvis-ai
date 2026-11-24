import requests

API_KEY = "cbfcb10953572ad1ec9bdedc179a12b1"


def get_weather(city="Chennai"):

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)

        data = response.json()

        if data.get("cod") != 200:

            return "Sorry boss, weather data is unavailable."

        temp = data["main"]["temp"]

        description = data["weather"][0]["description"]

        feels_like = data["main"]["feels_like"]

        return (
            f"The temperature in {city} is "
            f"{temp:.1f} degrees Celsius. "
            f"It feels like {feels_like:.1f} degrees. "
            f"Current condition is {description}."
        )

    except Exception as e:

        print("WEATHER ERROR:", e)

        return "Sorry boss, I could not get the weather."