import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=39b7889870abddd07e6655903a1bd0cd&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f" Temperature : {data['main']['temp']} C")
        print(f" Feels Like  : {data['main']['feels_like']} C")
        print(f" min temp : {data['main']['temp_min']} C")
    except requests.exceptions.RequestException as e:
        print(e)

city = input("Enter city name ")
weather_data(city)