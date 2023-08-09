from sqlalchemy.orm import sessionmaker
from db.models import User
from db.models import engine 
from api import fetch_weather
from simple_chalk import chalk

def add_user(username):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_username = input("Enter a new username: ")
    new_user = User(username=new_username)
    session.add(new_user)
    session.commit()
    
    # session.close()

def app_welcome():
    print("")
    print(chalk.green("Welcome! Please select a option: "))
    print(chalk.green("1: Get weather  2: login  3: quit"))
    print("")
    selection = input()
    if selection == "1" or selection.lower() == "get weather":
        fetch_weather()
    elif selection =="2" or selection == "login":
        add_user()
    elif selection =="3" or selection == "quit":
        exit()
