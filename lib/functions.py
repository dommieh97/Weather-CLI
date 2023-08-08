import time
from db.models import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()


weather_data = ["some", "weather", "stuff"]


def app():
    print("")
    print("Welcome to the app!  Please select a option: ")
    print("1: add  2: login  3: quit")
    print("")
    selection = input()
    if selection == "1" or selection == "add":
        add()
    elif selection =="2" or selection == "login":
        login()


def login():
    print("")
    print("Please enter your username or type new")
    # all_current_users = session.query(User)
    current_usernames = [user.username for user in session.query(User)]
    print("Current users:")
    print(current_usernames)
    input1 = input()
    if input1 == "new":
        print("please type a new username:")
        input2 = input()
        new_user = User(username=input2)
        session.add(new_user)
        session.commit()
        show_weather_details()
    elif input1 in current_usernames:
        show_weather_details()
    else:
        print("")
        print("Invalid input")
        time.sleep(0.55)
        app()


def show_weather_details():
    print("")
    print("Here is your weather details!")
    print("")
    print([detail for detail in weather_data])
    print("")
    print("Exit(1) or Go back(2)")
    input1 = input()
    if input1 == "2" or input1 == "go back":
        app()



def add():
    print("Please type some inputs to add:")
    x = input()
    y = input()  
    try:
        x = int(x)
        y = int(y)
        result = int(x) + int(y)
    except:
        result = "Both inputs must be integers"
    print("")
    print(f"This is your sum: {result}")
    app()