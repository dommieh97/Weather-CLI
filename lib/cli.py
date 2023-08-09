#!/usr/bin/env python3

from functions import app_welcome
from simple_chalk import chalk


if __name__ == '__main__':
    print(chalk.green("Welcome!"))
    app_welcome()    
    print(chalk.green("Bye!"))