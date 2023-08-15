import os
import requests

API_KEY = os.environ["API_KEY"]
BASE_URL = f"http://api.weatherstack.com/current?access_key={API_KEY}"


def fetch_weather_info(city=None, country=None):
    """
    Fetch weather info from API and return both response json and success status.
    Parameters:
    city
    country
    ---
    Returns
    Data dict
    Success status boolean
    """
    query = f"{city},{country}"

    if not all([city, country]):
        query = "fetch:ip"

    api_url = f"{BASE_URL}&query={query}"
    response = requests.get(api_url)
    res_json = response.json()

    if "success" not in res_json:
        info_of_city_weather = res_json["current"]
        info_of_city_location = res_json["location"]

        temperature = info_of_city_weather["temperature"]
        weather_desc = info_of_city_weather["weather_descriptions"]
        wind_speed = info_of_city_weather["wind_speed"]
        humidity = info_of_city_weather["humidity"]
        feels_like = info_of_city_weather["feelslike"]

        time = info_of_city_location["localtime"]
        city_name = info_of_city_location["name"]
        country_name = info_of_city_location["country"]

        return {
            "temperature": temperature,
            "weather_desc": weather_desc,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "feels_like": feels_like,
            "localtime": time,
            "city_name": city_name,
            "country_name": country_name
        }, True
    else:
        return res_json["error"], False


def format_response_text(info, status):
    if status:
        return "\n".join([
            "-"*20,
            f"Temperature: {info['temperature']}",
            f"Weather Description: {','.join(info['weather_desc'])}",
            f"Wind Speed: {info['wind_speed']}",
            f"Humidity: {info['humidity']}",
            f"Feels Like: {info['feels_like']}",
            f"Local Time: {info['localtime']}",
            f"The city and country you searched for are {info['city_name']}, {info['country_name']}"
        ])
    return f"Error: {info['info']}"


if __name__ == "__main__":
    while True:
        print("Welcome")
        print("Choose one option from the list",
              "1. Auto", "2. Type your city", sep="\n")

        user_input = input("Enter your answer: ")

        if user_input == "1":
            response, status = fetch_weather_info()
            print(format_response_text(response, status))
            break

        elif user_input == "2":
            user_city = input("Enter your city: ")
            user_country = input("Enter your country: ")
            response, status = fetch_weather_info(user_city, user_country)
            print(format_response_text(response, status))
            break

        else:
            print(">"*10, "Invalid option.")
