#!/usr/bin/env python3
import pyfiglet
from functions import menu
from simple_chalk import chalk

hi = f"{pyfiglet.figlet_format('WELCOME')}\n\n"

if __name__ == '__main__':
    print(chalk.green(hi))
    menu()    
