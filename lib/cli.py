from api import output as out
from api import response as resp
from simple_chalk import chalk

def get_city_input():
    return input(chalk.green("Enter a city: "))

def show_main_menu():
    return input(chalk.green("Enter 1 to try again or 2 for main menu: "))

if resp.status_code != 200:
    print(chalk.red("Sorry, No information is available because you are illiterate. Try again after looking up how to spell. Thank You!"))
    city = get_city_input()
    print(chalk.blue(out))
elif resp.status_code == 200:
    choice = show_main_menu()
    if choice == '1':
        city = ""
        city = get_city_input()
        print(chalk.blue(out))
    elif choice == '2':
        print("Main menu go brrrrrrr.")  
    else:
        print(chalk.red("Invalid choice. Please enter 1 or 2."))
        choice = show_main_menu()
        if choice == '1':
            city = get_city_input()
            print(chalk.blue(out))
        elif choice == '2':
            print("Main menu go brrrrrrr.") 
        else:
            print(chalk.red("Invalid choice. Please enter 1 or 2."))

else:
    print("Unhandled response status code.")