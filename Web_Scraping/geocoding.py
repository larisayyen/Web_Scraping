
import requests

def coordinates():

    address = input("What's your address?\n>")

    url = "https://nominatim.openstreetmap.org"

    response = requests.get(url,
                            params = {
                                'q': address,
                                'format':'json'
                            }).json()

    return f" lat: {response[0]['lat']}, lon: {response[0]['lon']}"

def address(lat,lon):

    url="https://nominatim.openstreetmap.org/reverse"

    response=requests.get(url,params={'lat':lat,'lon':lon,'format':'json'}).json()

    return response['display_name']
