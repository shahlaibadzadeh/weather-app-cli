import requests
import socket

API_KEY = "aa799c2b049a5a614c96bffb10b1f7ef"
url = "http://api.weatherstack.com/current"

# def get_user_ip():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address


def fetch_api_with_city(city, country):
    city = city
    country = country

    api_url = f"{url}?access_key={API_KEY}&query={city},{country}"
    response = requests.get(api_url)
    return response


def fetch_api_with_ip():
    api_url = f"{url}?access_key={API_KEY}&query=fetch:ip"
    response = requests.get(api_url)
    return response


def get_data_from_api(response):
    if response.status_code == 200:
        info_of_city_weather = response.json()["current"]
        temperature = info_of_city_weather["temperature"]
        weather_desc = info_of_city_weather["weather_descriptions"]
        wind_speed = info_of_city_weather["wind_speed"]
        humidity = info_of_city_weather["humidity"]
        feels_like = info_of_city_weather["feelslike"]
        time = response.json()["location"]["localtime"]

        return {"temperature": temperature, "weather_desc": weather_desc, "wind_speed": wind_speed, "humidity": humidity, "feels_like": feels_like, "localtime": time}
    else:
        return None


def get_city_from_user():
    user_city = input("Enter your city: ")
    user_country = input("Enter your country: ")
    return user_city, user_country


if __name__ == "__main__":
    while True:

        print("Welcome")
        print("Choose one option from the list \n 1. Auto \n 2. Type your city")

        user_input = input("Enter your answer: ")
        if user_input == "2":
            user_city, user_country = get_city_from_user()
            data_of_city = get_data_from_api(
                fetch_api_with_city(user_city, user_country))

            print(f'\nTemperature: {data_of_city["temperature"]}\nWeather Description: {",".join(data_of_city["weather_desc"])}\nWind Speed: {data_of_city["wind_speed"]}\nHumidity: {data_of_city["humidity"]}\nFeels Like: {data_of_city["feels_like"]}\nLocal Time: {data_of_city["localtime"]}')
            break

        elif user_input == "1":
            data_of_ip = get_data_from_api(fetch_api_with_ip())
            print(f'\nTemperature: {data_of_ip["temperature"]}\nWeather Description: {",".join(data_of_ip["weather_desc"])}\nWind Speed: {data_of_ip["wind_speed"]}\nHumidity: {data_of_ip["humidity"]}\nFeels Like: {data_of_ip["feels_like"]}\nLocal Time: {data_of_ip["localtime"]}')
            break

        else:
            print(">"*10, "Invalid option.")
