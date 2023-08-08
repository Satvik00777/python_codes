import requests

def get_weather_data(city_or_zip, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    if city_or_zip.isdigit():  # User input is a zip code
        params = {'zip': city_or_zip, 'appid': api_key}
    else:  # User input is a city name
        params = {'q': city_or_zip, 'appid': api_key}
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data

def display_weather(data):
    if data['cod'] == '404':
        print("City not found. Please try again.")
    else:
        city_name = data['name']
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city_name}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    
    user_input = input("Enter the name of a city or a zip code: ")
    weather_data = get_weather_data(user_input, api_key)
    display_weather(weather_data)
