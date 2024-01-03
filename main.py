import requests
import datetime
from config import open_weather_token

def get_solar_data(lat, lon, open_weather_token):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}"
        r = requests.get(url)
        data = r.json()

        weather = data["weather"][0]["description"]
        cur_weather = data["main"]["temp"]
        clouds = data["clouds"]["all"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Інформація від сонячної панелі:\n\tЗагальний опис погоди: {weather}\n\tКількість хмар: {clouds}\n\t"
              f"Температура повітря: {cur_weather} °F\n\tВологість: {humidity}%\n\tТиск: {pressure} мм рт.ст.\n\t"
              f"Швидкість вітру: {wind} м/с\n\tСхід сонця: {sunrise_timestamp}\n\tЗахід сонця: {sunset_timestamp}")

    except Exception as ex:
        print(ex)
        print("Check your latitude or longitude")

def main():
    lat = input("Введіть широту: ")
    lon = input("Введіть довготу: ")
    get_solar_data(lat, lon, open_weather_token)

if __name__ == '__main__':
    main()
