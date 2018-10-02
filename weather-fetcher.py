#!/usr/bin/env python3

from weather import Weather, Unit

print ("\t\t\t\t\t Welcome to the weather forecast station..")

print ("\n\n \t\t\t\t\t Developed and Maintained by Chirag Gupta.. ")

print(" \n\n\t\t\t Enter the desired city name to continue..")

# block 1: City input

city = str(raw_input ('\n Enter the city name '))
print (city)
weather = Weather(unit=Unit.CELSIUS)
print("The weather in " + city + " will be : " )
location = weather.lookup_by_location('city')
condition = location.condition
print(condition.text)

print("\n Would you like to recieve " + city + "\'s upcoming week updates. Please Enter Y for yes and N for no")

choice = str(raw_input())
 
if (choice == 'Y' or choice == 'yes' or choice == 'y' or choice == 'Yes'):
    print(" \n\t\t\t\t Your upcoming week weather forecast is : ")
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('city')

    forecasts = location.forecast
    for forecast in forecasts:
        print(forecast.text)
        print(forecast.date)
        print(forecast.high)
        print(forecast.low)
else:
    print("Thanks for using this application")

