import requests
import argparse
import pyfiglet
from simple_chalk import chalk
BASE_URL = "http://api.weatherapi.com/v1/current.json?key=e984033b925f443ebc1211505230608"

no = f"{pyfiglet.figlet_format('GOODBYE')}\n\n"
def byebye():
    print(chalk.red.bold(no))
    exit()


def fetch_weather():
    from functions import is_logged_in
    if is_logged_in == True: 
        from functions import units, humids, precips,feels, visibs
    global city
    global region
    global country
    try:
        city = input(chalk.green.bold("Type a city here: "))
        url = f"{BASE_URL}&q={city}&aqi=no"

        response = requests.get(url)
        data = response.json()

        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        if is_logged_in:
            if units is not None:
                if units == "1" or units == "metric":
                    temp = str(data["current"]["temp_c"]) + "C"
                else:
                    temp = str(data["current"]["temp_f"]) + "F"
            else:
                temp = str(data["current"]["temp_f"]) + "F"
        else:
            temp = str(data["current"]["temp_f"]) + "F"
        local_time = data["location"]["localtime"]
        if is_logged_in:
            if units is not None:
                if units == "1" or units == "metric":
                    wind = str(data["current"]["wind_kph"]) + "KPH"
                else:
                    wind = str(data["current"]["wind_mph"]) + "MPH"
            else:
                wind = str(data["current"]["wind_mph"]) + "MPH"
        else:
            wind = str(data["current"]["wind_mph"]) + "MPH"
        wind_dir = data["current"]["wind_dir"]
        if is_logged_in: 
            if precips != "2" and precips is not None:
                if units == "1":
                    precip = str(data["current"]["precip_mm"])+"mm"
                else:
                    precip = str(data["current"]["precip_in"])+"in"
            else:
                pass
        else:
            pass
        if is_logged_in: 
            if humids != "2" and humids is not None:
                if units == "1":
                    humidity = data["current"]["humidity"]
                else:
                    pass
            else:
                pass
        current_condition = data['current']['condition']["text"]
        if is_logged_in:
            if feels != "2" and feels is not None:
                if units == "1":
                    feels_like = str(data['current']['feelslike_c'])+"C"
                else:
                    feels_like = str(data['current']['feelslike_f'])+"F"
            else:
                pass
        else:
            pass
        if is_logged_in: 
            if visibs != "2" and visibs is not None:
                if units == "1":
                    vis = str(data['current']['vis_km'])+"KM"
                else :
                    vis = str(data['current']['vis_miles'])+"miles"
            else:
                pass
        else:
            pass
        
        
        output = f"{pyfiglet.figlet_format(location)}{pyfiglet.figlet_format(region)}{pyfiglet.figlet_format(country)}\n\n"
        output += f"Temperature: {temp}\n\n"
        if is_logged_in:
            if feels != "2" and feels is not None:
                output += f"Temperature feels like: {feels_like}\n\n"
        output += f"Local Time: {local_time}\n\n"
        output += f"Current Wind: {wind} {wind_dir}\n\n"
        if is_logged_in:
            if precips != "2" and precips is not None:
                output += f"Current Precipitation: {precip}\n\n"
        if is_logged_in:        
            if  humids != "2" and humids is not None:
                output += f"Current Humidity: {humidity}\n\n"
        if is_logged_in:
            if visibs != "2" and visibs is not None:
                output += f"Current visibility: {vis}\n\n"
        output += f"Current Condition: {current_condition}: "

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
        print(chalk.blue.bold(output))
        if response.status_code == 200:
            good_response_code()
    except KeyError:
            print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
            fetch_weather()

def get_city_input():
    return input(chalk.green.bold("Enter a city: "))

def show_main_menu():
    from functions import is_logged_in
    return input(chalk.green(f'Enter 1 to try again, 2 for main menu, {"3 save city, or 4 to quit"if is_logged_in == True else "or 3 to quit"}: \n'))

def bad_status_code():
    print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
    fetch_weather()

def store_city(city_name,region,country):
    from functions import is_logged_in, session, current_user
    from db.models import User, City
    
    if is_logged_in and current_user:
        user = session.query(User).filter(User.id == current_user.id).first()
        if user:
            is_cities = [city.name for city in user.cities]
            if city_name not in is_cities:
                new_city = City(name=city_name, region=region, country=country)
                user.cities.append(new_city)
                session.commit()
                print(chalk.green.bold(f"{city_name} has been saved"))
            else:
                print(chalk.red("City is already in database"))
        else:
            print(chalk.red("User not found"))
    else:
        print(chalk.red("Login to save city"))

def process_choice(choice):
    from functions import menu, is_logged_in
    if choice == '1':
        fetch_weather()
    elif choice == '2':
        menu()
    elif choice == '3':
        if is_logged_in:
            store_city(city, country,region)
        else:
            byebye()
    elif choice == '4':
        if is_logged_in == True:
            byebye()
        else:
            print(chalk.red(f"Invalid choice. Please enter 1, 2, or 3. Or else I'm kicking you out >:("))


def good_response_code():
    from functions import is_logged_in
    while True:
        choice = show_main_menu()
        if choice in (f'1 , 2, {"3 , 4"if is_logged_in == True else "3" } \n'):
            process_choice(choice)
        else:
            print(chalk.red(f"Invalid choice. Please enter 1, 2, {'3 or 4' if is_logged_in == True else 'or 3'}. Or else I'm kicking you out >:(\n"))
        

if __name__ == "__main__":
    good_response_code()
    