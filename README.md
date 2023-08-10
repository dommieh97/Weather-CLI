Weather CLI Application

Introduction:
This is a weather CLI application. 
    You are able to:
        -Create User:
        -Set Preferences
        -View Weather
        -Save and View Saved City

In order to run this app make sure to pipenv install and run pipenv shell

Functionalities

Option 1: Get Weather

Function: fetch_weather()
Description: This function retrieves current weather information for a specified city using the Weather API. It prompts the user to input a city name, fetches the weather data, and displays relevant details such as temperature, wind speed, humidity, and more. The weather conditions are represented by corresponding emojis.
Option 2: Preferences/Login

Function: add_preference() and login()
Description:
add_preference(): This function allows a logged-in user to customize their weather display preferences. It prompts the user to choose metric or imperial units, precipitation, humidity, feels-like temperature, and visibility preferences.
login(): This function handles user authentication. It prompts the user to log in with an existing username or create a new user. Upon successful login or creation, it sets the user as logged in and provides access to personalized preferences and other options.
Option 3: My Cities

Function: my_cities()
Description: This function displays a list of cities that the logged-in user has saved to their preferences. If the user has saved cities, it lists them; otherwise, it informs the user that no cities are saved.
Option 4: Quit

Function: byebye()
Description: This function terminates the application with a "GOODBYE" message. It's used to gracefully exit the program when the user chooses to quit.

Credits to:
    Dom
    Tim
    Mark
LinkedIn for Tim: https://www.linkedin.com/in/timothy-mueller-089500281
LinkedIn for Mark: https://www.linkedin.com/in/mark-john-tocino-7b6649259/
LinkedIn for Dom: https://www.linkedin.com/in/domenique-hester-ba9498179/

Weather API = https://www.weatherapi.com
Key = e984033b925f443ebc1211505230608