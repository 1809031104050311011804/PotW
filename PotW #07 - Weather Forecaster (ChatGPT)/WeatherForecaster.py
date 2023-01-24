import os
import requests
import json


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def location():
    global location_user, latitude, longitude
    
    # Enter the location you want to look up
    location_user = input("\nWhat location in the United States would you like to see the 5-day forecast for?\n")

    try:
        # Make the API request
        response = requests.get(f"https://nominatim.openstreetmap.org/search?q={location_user}&format=json")
    except:
        print("ERROR: API REQUEST FAILED\n")
        exit()

    try:
        # Get the response data as a Python dictionary
        data = response.json()
        
        # Get the first result from the list of results
        result = data[0]

        # Get the latitude and longitude from the result
        latitude = result['lat']
        longitude = result['lon']
    except:
        print("ERROR: INVALID LOCATION")
        location()

    forecast()


def forecast():
    # Make the API request
    try:
        response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    except:
        print("ERROR: API REQUEST FAILED\n")
        exit()    

    try:
        # Get the response data as a Python dictionary
        data = response.json()

        # Get the URL for the forecast
        forecast_url = data['properties']['forecast']

        # Make the API request for the forecast
        response = requests.get(forecast_url)

        # Get the response data as a Python dictionary
        data = response.json()

        # Get the forecast data
        forecasts = data['properties']['periods']
    except:
        print("ERROR: INVALID LOCATION")
        location()

    # Print the forecast for each day
    clear()

    print(f"The 5-day forcecast for {location_user} is:\n")
    
    for forecast in forecasts:
        temperature = forecast['temperature']
        description = forecast['shortForecast']
        name = forecast['name']
        print(f"{name}: {temperature}°F with {description}")

    forecast_again()


def forecast_again():
    again = input("\nWould you like to see another 5-day forecast? (Y/N)\n").upper()

    if again == "Y":
        location()
    elif again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID INPUT")
        forecast_again()


location()
