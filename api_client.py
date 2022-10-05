import requests
import datetime

key = "660fe8f4b15c4461b70135330220510"
api_url = f"http://api.weatherapi.com/v1"


def get_current_temperature(city):
    response = requests.get(api_url + f"/current.json?key={key}&q={city}")
    res = response.json()
    print(res["current"])

    return res["current"]


def get_temperature_after(city, days, hours=None):

    start_date = datetime.datetime.today().date()
    date_1 = datetime.datetime.strptime(str(start_date), "%Y-%m-%d")

    end_date = date_1 + datetime.timedelta(days=days)

    print(end_date)

    response = requests.get(api_url + f"/future.json?key={key}&q={city}&dt={end_date}&hour={hours}")
    res = response.json()
    print(res["forecast"]["forecastday"])
    return res["forecast"]["forecastday"]

# get_temperature_after("", "")


def get_lat_and_long(city):
    response = requests.get(api_url + f"/current.json?key={key}&q={city}")
    res = response.json()

    return res["location"]["lat"], res["location"]["lon"]


# get_lat_and_long("london")
# get_current_temperature("london")
# get_temperature_after("london", 15, 12)
