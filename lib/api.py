import requests
import argparse
import pyfiglet
from simple_chalk import chalk

BASE_URL = "http://api.weatherapi.com/v1/current.json?key=e984033b925f443ebc1211505230608"

no = f"{pyfiglet.figlet_format('GOODBYE')}\n\n"

def byebye():
    print(chalk.red(no))
    exit()


def fetch_weather():
    try:
        city = input(chalk.green("Type a city here: "))
        url = f"{BASE_URL}&q={city}&aqi=no"

        response = requests.get(url)
        data = response.json()

        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        # lat = data["location"]["lat"]
        # lon = data["location"]["lon"]
        # tz = data["location"]["tz_id"]
        # localtime = data["location"]["localtime"]
        temp_f = data["current"]["temp_f"]
        # temp_c = data["current"]["temp_c"]
        local_time = data["location"]["localtime"]
        wind_mph = data["current"]["wind_mph"]
        # wind_kph = data["location"]["wind_kph"]
        # wind_dir = data["location"]["wind_dir"]
        # precip_mm = data["location"]["precip_mm"]
        # precip_in = data["location"]["precip_in"]
        # humidity = data["location"]["humidity"]
        # cloud = data["location"]["cloud"]
        current_condition = data['current']['condition']["text"]
        # feels_like_c = data['current']['feels_like_c']
        # feels_like_f = data['current']['feels_like_f']
        # vis_km = data['current']['vis_km']
        # vis_miles = data['current']['vis_miles']
        # uv = data['current']['uv']



        output = f"{pyfiglet.figlet_format(location)}, {pyfiglet.figlet_format(region)},{pyfiglet.figlet_format(country)}\n\n"
        output += f"Temperature {temp_f}F\n\n"
        output += f"Local Time {local_time}\n\n"
        output += f"Current Wind in MPH {wind_mph}mph\n\n"
        output += f"Current Condition {current_condition} : "

        if data:
            if data["current"]["condition"]["text"] == "Sunny":
                output += "☀️"
            elif data["current"]["condition"]["text"] == "Partly cloudy":
                output += "⛅"
            elif data["current"]["condition"]["text"] == "Cloudy":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Overcast":
                output += "⛅"
            elif data["current"]["condition"]["text"] == "Mist":
                output += "⛆"
            elif data["current"]["condition"]["text"] == "Pathcy rain possible":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Patchy snow possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy sleet possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy freezing drizzle possible":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Thundery outbreaks possible":
                output += "🌩"
            elif data["current"]["condition"]["text"] == "Blowing snow":
                output += "🌬"
            elif data["current"]["condition"]["text"] == "Blizzard":
                output += "⛇"
            elif data["current"]["condition"]["text"] == "Fog":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Freezing fog":
                output += "☁"
            elif data["current"]["condition"]["text"] == "Patchy light drizzle":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Light drizzle":
                output += "🌦"
            elif data["current"]["condition"]["text"] == "Freezing drizzle":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy freezing drizzle":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Patchy light rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate rain at times":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy rain at times":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Heavy rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light freezing rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy freezing rain":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light sleet":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy sleet":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Patchy light snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy moderate snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy heavy snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Heavy snow":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Moderate or heavy rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Torrential rain shower":
                output += "🌧"
            elif data["current"]["condition"]["text"] == "Light sleet showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy sleet showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light snow showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy snow showers":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Light showers of ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Moderate or heavy showers of ice pellets":
                output += "🌨"
            elif data["current"]["condition"]["text"] == "Patchy light rain with thunder":
                output += "⛈"
            elif data["current"]["condition"]["text"] == "Moderate or heavy rain with thunder":
                output += "⛈"
            elif data["current"]["condition"]["text"] == "Patchy light snow with thunder":
                output += "⛈☃"
            elif data["current"]["condition"]["text"] == "Moderate or heavy snow with thunder":
                output += "⛈☃"
            elif data["current"]["condition"]["text"] == "Clear":
                output += "🌝"
        print(chalk.blue(output))
    
            
        if response.status_code == 200:
            good_response_code()
    except KeyError:
            raise KeyError

def get_city_input():
    return input(chalk.green("Enter a city: "))

def show_main_menu():
    return input(chalk.green("Enter 1 to try again, 2 for main menu, or 3 to quit : "))

def bad_status_code():
    print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
    fetch_weather()


def process_choice(choice):
    from functions import menu
    if choice == '1':
        fetch_weather()
    elif choice == '2':
        menu()
    elif choice == '3':
        byebye()

def good_response_code():
    while True:
        choice = show_main_menu()
        if choice in ('1', '2', '3'):
            process_choice(choice)
        else:
            print(chalk.red("Invalid choice. Please enter 1, 2, or 3. Or else I'm kicking you out >:("))
        

if __name__ == "__main__":
    good_response_code()