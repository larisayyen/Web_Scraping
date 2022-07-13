
import csv,sys
import datetime
import requests
import urllib.parse
from weather.forecast_city import search_city
from weather.forecast_city import BASE_URL

def daily_forecast(woeid,year,month,day):

    url = urllib.parse.urljoin(BASE_URL,f"api/location/{woeid}/{year}/{month}/{day}")
    return requests.get(url).json()

# get a weather list for a whole month
def monthly_forecast(woeid,year,month):

    # set up
    forecasts = []
    date = datetime.date(year,month,1)

    # aggregate date
    if month == 12:
        upper_bound = datetime.date(year+1,1,1)
    else:
        upper_bound = datetime.date(year,month+1,1)

    # fulfill the list
    while date < upper_bound:
        print(f"weather forecast for {date.strftime('%Y-%m-%d')}")
        forecasts += daily_forecast(woeid,date.year,date.month,date.day)
        date = date + datetime.timedelta(days = 1)

    return forecasts


def write_csv(woeid, year, month, city, forecasts):

    filename=f"{year}_{'{:02d}'.format(month)}_{woeid}_{city.lower()}"
    with open(f"data/{filename}.csv","w") as output_file:
        keys=forecasts[0].keys()
        dict_writer=csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(forecasts)

def main():
    if len(sys.argv) > 2:
        city = search_city(sys.argv[1])
        if city:
            woeid = city['woeid']
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            if 1 <= month <= 12:
                forecasts = monthly_forecast(woeid, year, month)
                if not forecasts:
                    print("Sorry, could not fetch any forecast")
                else:
                    write_csv(woeid, year, month, city['title'], forecasts)
            else:
                print("MONTH must be a number between 1 (Jan) and 12 (Dec)")
                sys.exit(1)
    else:
        print("Usage: python history.py CITY YEAR MONTH")
        sys.exit(1)

if __name__ == "__main__":
    main()
