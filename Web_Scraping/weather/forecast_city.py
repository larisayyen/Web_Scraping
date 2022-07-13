
import sys
import urllib.parse
import requests

BASE_URL = "https://www.metaweather.com"

# query a city
def search_city(query):

    url = urllib.parse.urljoin(BASE_URL,f'api/location/search/?query={query}')
    cities = requests.get(url).json()

    if not cities:
        print(f"{query} not found.")
        return None

    elif len(cities) == 1:
        return cities[0]

    else:
        for i,city in enumerate(cities):
            print(f"{i+1}.{city['title']}")
        index = int(input("Which city do you choose?")) - 1
        return cities[index]

def weather_forecast(woeid):

    url=urllib.parse.urljoin(BASE_URL,f"api/location/{woeid}")
    response=requests.get(url).json()
    return response['consolidated_weather']

def main():

    query = input('Which city do you want to search?\n>')
    city = search_city(query)
    weathers = weather_forecast(city.get('woeid'))

    print(f"Here's the weather in {city.get('title')}")

    for weather in weathers:
        print(f"{weather.get('applicable_date')}: {weather.get('weather_state_name')} {weather.get('the_temp')} °C\n")

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nOops!')
        sys.exit()
