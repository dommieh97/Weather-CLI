#!/usr/bin/env python3

from api import fetch_weather
from functions import app
from simple_chalk import chalk


if __name__ == '__main__':
    print(chalk.green("Welcome!"))
    fetch_weather()
    print(chalk.green("Bye!"))