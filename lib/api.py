import requests

api_url = "http://api.weatherapi.com/v1/current.json?key=e984033b925f443ebc1211505230608&q=Houston&aqi=no"

def fetch_data_with_api_key(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()     
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

data = fetch_data_with_api_key(api_url)

if data:
    # Do something with the fetched data
    print(data["location"])
    # print(data["current"])
    # apple = data["current"]
    # print(data)
    if data["current"]["condition"]["text"] == "Sunny":
        print("☀️")
    elif data["current"]["condition"]["text"] == "Partly cloudy":
        print("⛅ ")
    elif data["current"]["condition"]["text"] == "Cloudy":
        print("☁")
    elif data["current"]["condition"]["text"] == "Overcast":
        print("⛅ ")
    elif data["current"]["condition"]["text"] == "Mist":
        print("⛆")
    elif data["current"]["condition"]["text"] == "Pathcy rain possible":
        print("🌦")
    elif data["current"]["condition"]["text"] == "Patchy snow possible":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Patchy sleet possible":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Patchy freezing drizzle possible":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Thundery outbreaks possible":
        print("🌩")
    elif data["current"]["condition"]["text"] == "Blowing snow":
        print("🌬")
    elif data["current"]["condition"]["text"] == "Blizzard":
        print("⛇")
    elif data["current"]["condition"]["text"] == "Fog":
        print("☁")
    elif data["current"]["condition"]["text"] == "Freezing fog":
        print("☁")
    elif data["current"]["condition"]["text"] == "Patchy light drizzle":
        print("🌦")
    elif data["current"]["condition"]["text"] == "Light drizzle":
        print("🌦")
    elif data["current"]["condition"]["text"] == "Freezing drizzle":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Heavy freezing drizzle":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Patchy light rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Light rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Moderate rain at times":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Moderate rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Heavy rain at times":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Heavy rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Light freezing rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Moderate or heavy freezing rain":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Light sleet":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Moderate or heavy sleet":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Patchy light snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Light snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Patchy moderate snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Moderate snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Patchy heavy snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Heavy snow":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Ice pellets":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Light rain shower":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Moderate or heavy rain shower":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Torrential rain shower":
        print("🌧")
    elif data["current"]["condition"]["text"] == "Light sleet showers":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Moderate or heavy sleet showers":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Light snow showers":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Moderate or heavy snow showers":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Light showers of ice pellets":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Moderate or heavy showers of ice pellets":
        print("🌨")
    elif data["current"]["condition"]["text"] == "Patchy light rain with thunder":
        print("⛈")
    elif data["current"]["condition"]["text"] == "Moderate or heavy rain with thunder":
        print("⛈")
    elif data["current"]["condition"]["text"] == "Patchy light snow with thunder":
        print("⛈☃")
    elif data["current"]["condition"]["text"] == "Moderate or heavy snow with thunder":
        print("⛈☃")

    