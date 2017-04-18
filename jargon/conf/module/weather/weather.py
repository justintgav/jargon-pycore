# Author: Ryan Lindsay and Justin Gavin
# Description: A module to handle weather information
#
# args format:
#   'weather_type': expecting the 'type' of weather information requested.
#                   Ex: 'rain', 'snow', 'temperature'
#                   '' will result in a general report
#   'location': the name of the city to use
#
# Example NL Queries:
#   What is the temperature in Glassboro NJ?
#    +args['weather_type'] = 'temperature'
#    +args['location'] = 'glassboro nj'
#   >> Current weather in Glassboro
#   >> Current temperature		65.08°F
#   >> Projected temperatures	High 66.2°F			Low 62.6°F

import datetime
import json
import urllib.request
import sys


# Used to convert time to a nice format for printing
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time


# Used to create the url used in the API call
def url_creator(city_name):
    url_base = 'http://api.openweathermap.org/data/2.5/weather?q='  # Base url. Queries are appended
    return_format = 'json'  # Can be changed if needed
    unit_of_measure = 'imperial'  # For Celsius use metric
    api_key = 'e04e1be973806b2dcc0a353dc78fc2c5'  # Personal key, please don't steal

    # Create the full url for the api call
    full_api_url = (url_base +
                    '?q=' + str(city_name) +
                    '&mode=' + str(return_format) +
                    '&units=' + str(unit_of_measure) +
                    '&APPID=' + api_key)
    return full_api_url


# Used to get the json object from the API call
def data_collector(full_api_url):
    open_url = urllib.request.urlopen(full_api_url)  # Open connection to website
    website_output = open_url.read().decode('utf-8')  # They use UTF-8 for decoding
    loaded_api_dict = json.loads(website_output)  # Decode json file
    open_url.close()  # Close connection to website
    return loaded_api_dict


# Used to define how to get certain information from the json object
def data_organizer(full_api_dict):
    return_data = dict(
        city=full_api_dict.get('name'),  # City of interest
        cloudiness=full_api_dict.get('clouds').get('all'),  # Percent cloudiness
        country=full_api_dict.get('sys').get('country'),  # Country that city is in
        temp=full_api_dict.get('main').get('temp'),  # Current temperature
        temp_max=full_api_dict.get('main').get('temp_max'),  # Temperature high
        temp_min=full_api_dict.get('main').get('temp_min'),  # Temperature low
        time=time_converter(full_api_dict.get('dt')),  # Time of server update
        humidity=full_api_dict.get('main').get('humidity'),  # Current humidity
        pressure=full_api_dict.get('main').get('pressure'),  # Current pressure
        sunrise=time_converter(full_api_dict.get('sys').get('sunrise')),  # Time sun will rise
        sunset=time_converter(full_api_dict.get('sys').get('sunset')),  # Time sun will set
        weather=full_api_dict['weather'][0]['main'],  # Sky status
        wind_speed=full_api_dict.get('wind').get('speed'),  # Current wind speed
        wind_dir=full_api_dict.get('deg'))  # Current wind direction

    # Optional rain parameter
    if full_api_dict.get('rain') is None:
        return_data['rain'] = '0'
    else:
        return_data['rain'] = full_api_dict.get('rain').get(['3h'])

    # Optional snow parameter
    if full_api_dict.get('snow') is None:
        return_data['snow'] = '0'
    else:
        return_data['snow'] = full_api_dict['snow'][0]['3h']

    return return_data


# Used to display the important information
def print_weather(data, data_type):
    temp_symbol = '\xb0' + 'F'  # Change to 'C' if Celsius is used
    info = str(data_type).lower()  # Information type required
    return_string = ''  # Final string that will be passed back

    # Nice little top border
    # return_string += '\n------------------------------------------------------------------------------'
    # return_string += '\nCurrent weather in {}-{}'.format(data['city'], data['country'])
    return_string += '\nCurrent weather in {}'.format(data['city'])

    # Opted for if-elif-else statement instead of a dictionary for readability
    if (info == "rain") or (info == "rainy") or (info == "rainfall"):
        return_string += '\nRain in the past three hours {}mm'.format(data['rain'])
    elif (info == "snow") or (info == "snowy") or (info == "snowfall"):
        return_string += '\nSnow in the past three hours {}mm'.format(data['snow'])
    elif (info == "sky") or (info == "clouds") or (info == "clear") or (info == "weather"):
        return_string += '\nCurrent sky condition  {}'.format(data['weather'])
        return_string += '\nCurrent cloud coverage {}%'.format(data['cloudiness'])
    elif (info == "temp") or (info == "temperature") or (info == "hot") or (info == "cool") or (info == "cold"):
        return_string += '\nCurrent temperature\t\t{}{}'.format(data['temp'], temp_symbol)
        return_string += '\nProjected temperatures\tHigh {}{}\t\t\tLow {}{}'.format(data['temp_max'], temp_symbol,
                                                                                    data['temp_min'], temp_symbol)
    else:
        return_string += '\nCurrent temperature\t\t\t{}{}'.format(data['temp'], temp_symbol)
        return_string += '\nProjected temperatures\t\tHigh {}{}\t\t\tLow {}{}'.format(data['temp_max'], temp_symbol,
                                                                                      data['temp_min'], temp_symbol)
        return_string += '\nCurrent sky conditions\t\t{}'.format(data['weather'])
        return_string += '\nCurrent cloud coverage\t\t{}%'.format(data['cloudiness'])
        return_string += '\nRain/Snow in past 3 hours\tRain: {}mm\t\t\tSnow: {}mm'.format(data['rain'], data['snow'])
        return_string += '\nWind speed/angle\t\t\tSpeed: {}mph\t\tAngle: {}\xb0'.format(data['wind_speed'],
                                                                                        data['wind_dir'])
        return_string += '\nHumidity/Pressure\t\t\tHumidity: {}%\t\tPressure: {}hPa'.format(data['humidity'],
                                                                                            data['pressure'])
        return_string += '\nSunrise/Sunset times\t\tSunrise: {}\tSunset: {}'.format(data['sunrise'], data['sunset'])

    return return_string


# Custom exception to ensure we don't go over limit
class WeatherAPILimit(Exception):
    """Only 10 API calls per minute allowed"""
    pass


# Custom exception to ensure we have enough info to process
class MinInfoLimit(Exception):
    """Must have at least three parameters"""
    pass


def module_main(args):
    try:
        # if len(sys.argv) > 62:  # Sixty API call per minute max
        #     raise WeatherAPILimit
        # elif len(sys.argv) < 3:  # Three parameters required min
        #     raise MinInfoLimit

        # Grab what type of data is important
        #  = sys.argv[1]
        data_wanted = args['weather_type']

        # Loop through each city and display data
        # for argument in sys.argv[2]:
        #    main_url = url_creator(argument)                                    # Assumes arguments are City names
        #    api_dict = data_collector(main_url)                                 # Grab base data file
        #    api_data = data_organizer(api_dict)                                 # Organize base data file
        #    final_string = print_weather(api_data, data_wanted)                 # Print information requested

        main_url = url_creator(args['location'])  # Assumes arguments are City names
        api_dict = data_collector(main_url)  # Grab base data file
        api_data = data_organizer(api_dict)  # Organize base data file
        final_string = print_weather(api_data, data_wanted)  # Print information requested

        # Print a notice and border bottom
        # final_string += '\n'
        # final_string += '\nServer last updated at {}'.format(api_data.get('time'))
        # final_string += '\n------------------------------------------------------------------------------'

        return final_string
        # final_string should at this point contain all information that should be displayed #

    # I'm not sure what should be done with exceptions
    except WeatherAPILimit:
        print('Up to 60 API calls per minute max')
    except MinInfoLimit:
        print('At least 3 parameters required to run')
    except IOError:
        print('Something went wrong with reading data')

# example calls
# print(module_main({'weather_type': 'temperature', 'location': 'glassboro nj'}))
# print(module_main({'weather_type': 'weather', 'location': 'glassboro nj'}))
# print(module_main({'weather_type': '', 'location': 'glassboro nj'}))
