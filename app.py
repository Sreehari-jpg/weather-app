import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
    except requests.exceptions.RequestException:
        return None, "Could not reach the weather service. Try again."

    if response.status_code == 404:
        return None, f"City '{city}' not found."
    if response.status_code != 200:
        return None, "Something went wrong with the weather service."

    data = response.json()
    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": round(data["main"]["temp"]),
        "feels_like": round(data["main"]["feels_like"]),
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
    }
    return weather, None


@app.route("/", methods=["GET", "POST"])
def index():
    weather, error = None, None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            weather, error = get_weather(city)
        else:
            error = "Please enter a city name."
    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)