"""
Title: Band Name Generator
Author: Michał Chojna
Date: 01.06.2022
Description: Creates name of a band from user's city's name and user's pet's name
"""

# Prints welcome message
print("Welcome to the Band Name Generator.")

# Takes the name of the user's city 
city = input("What is the name of the city you grew up in? ")

# Takes the name of the user's pet 
name = input("What is your pet's name? ")

# Prints the name of the band created from user's city name and user's pet name
print("Your band name could be: " + city + " " + name)
