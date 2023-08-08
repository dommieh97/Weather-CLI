import requests
import argparse
import pyfiglet
from simple_chalk import chalk

BASE_URL = "http://api.weatherapi.com/v1/current.json?key=e984033b925f443ebc1211505230608"

no = f"{pyfiglet.figlet_format('GOODBYE')}\n\n"


def fetch_weather():
    city = input(chalk.green("Type a city here: "))
    url = f"{BASE_URL}&q={city}&aqi=no"

    response = requests.get(url)
    data = response.json()

    location = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    feels_like = data["current"]["temp_f"]
    local_time = data["location"]["localtime"]
    wind_mph = data["current"]["wind_mph"]
    current_condition = data['current']['condition']["text"]

    output = f"{pyfiglet.figlet_format(location)}, {pyfiglet.figlet_format(region)},{pyfiglet.figlet_format(country)}\n\n"
    output += f"Temperature {feels_like}F\n\n"
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

    if response.status_code != 200:
        bad_status_code()
    elif response.status_code == 200:
        good_responce_code()
    else:
        print("Unhandled response status code.")


def get_city_input():
    return input(chalk.green("Enter a city: "))

def show_main_menu():
    return input(chalk.green("Enter 1 to try again or 2 for main menu: "))

def bad_status_code():
    print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
    fetch_weather()

def good_responce_code():
    choice = show_main_menu()
    if choice == '1':
        fetch_weather()
    elif choice == '2':
        print(chalk.magentaBright("Main menu go brrrrrrr.")) 
    else:
        print(chalk.red("Invalid choice. Please enter 1 or 2."))
        choice = show_main_menu()
        if choice == '1':
            fetch_weather()
        elif choice == '2':
            print(chalk.magentaBright("Main menu go brrrrrrr.")) 
        else:
            print(chalk.red("Invalid choice. Please enter 1 or 2. Or else i'm kicking you out >:("))
            choice = show_main_menu()
            if choice == '1':
                fetch_weather()
            elif choice == '2':
                print(chalk.magentaBright("Main menu go brrrrrrr.")) 
            else:
                print(chalk.redBright.bold(no))