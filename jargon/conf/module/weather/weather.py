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


# Used to convert time to a nice format for printing
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time


# Used to create the url used in the API call
def url_creator(city_name, time_frame):
    url_base = 'http://api.openweathermap.org/data/2.5/'  # Base url. Queries are appended
    return_format = 'json'  # Can be changed if needed
    unit_of_measure = 'imperial'  # For Celsius use metric
    api_key = 'e04e1be973806b2dcc0a353dc78fc2c5'  # Personal key, please don't steal

    # Determine if regular weather is needed or 5-day
    if time_frame == 'five_day':
        weather_type = 'forecast'
    else:
        weather_type = 'weather'

    # Create the full url for the api call
    full_api_url = (url_base + str(weather_type) +
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


# Used to collect appropriate data from json object per weather query
def data_organizer_current(full_api_c):
    return_data = dict(
        city=full_api_c.get('name'),  # City of interest
        cloudiness=full_api_c.get('clouds').get('all'),  # Percent cloudiness
        temp=full_api_c.get('main').get('temp'),  # Current temperature
        temp_max=full_api_c.get('main').get('temp_max'),  # Temperature high
        temp_min=full_api_c.get('main').get('temp_min'),  # Temperature low
        time=time_converter(full_api_c.get('dt')),  # Time of server update
        humidity=full_api_c.get('main').get('humidity'),  # Current humidity
        pressure=full_api_c.get('main').get('pressure'),  # Current pressure
        sunrise=time_converter(full_api_c.get('sys').get('sunrise')),  # Time sun will rise
        sunset=time_converter(full_api_c.get('sys').get('sunset')),  # Time sun will set
        weather=full_api_c['weather'][0]['main'],  # Sky status
        wind_speed=full_api_c.get('wind').get('speed'),  # Current wind speed
        wind_dir=full_api_c.get('deg'))  # Current wind direction

    # Optional rain parameter
    if full_api_c.get('rain') is None:
        return_data['rain'] = '0'
    else:
        return_data['rain'] = full_api_c.get('rain').get(['3h'])

    # Optional snow parameter
    if full_api_c.get('snow') is None:
        return_data['snow'] = '0'
    else:
        return_data['snow'] = full_api_c['snow'][0]['3h']

    return return_data


# Used to collect appropriate data from json object per forecast query
def data_organizer_span(full_api_s):
    api_list = full_api_s.get('list')

    # This is ugly and I would like a better way if possible @Johan
    all_cloudiness = []
    all_temp = []
    all_temp_max = []
    all_temp_min = []
    all_time = []
    all_humidity = []
    all_pressure = []
    all_weather = []
    all_wind_speed = []
    all_wind_dir = []

    # The number of entries for weather information
    list_len = len(api_list)  # There's a random message at the end that shouldn't be included

    # Loop through all the values given and add them to the list
    for item in range(0, list_len):
        all_cloudiness.append(api_list[item].get('clouds').get('all'))
        all_temp.append(api_list[item].get('main').get('temp'))
        all_temp_max.append(api_list[item].get('main').get('temp_max'))
        all_temp_min.append(api_list[item].get('main').get('temp_min'))
        all_time.append(time_converter(api_list[item].get('dt')))
        all_humidity.append(api_list[item].get('main').get('humidity'))
        all_pressure.append(api_list[item].get('main').get('pressure'))
        all_weather.append(api_list[item].get('weather')[0]['main'])
        all_wind_speed.append(api_list[item].get('wind').get('speed'))
        all_wind_dir.append(api_list[item].get('wind').get('deg'))

    # Create the dictionary object that is to be returned
    return_data = dict(
        city=full_api_s.get('city').get('name'),  # City of interest
        cloudiness=all_cloudiness,  # Add the list of cloudiness
        temp=all_temp,  # Add the list of temperatures
        temp_max=all_temp_max,  # Add the list of max temperatures
        temp_min=all_temp_min,  # Add the list of min temperatures
        humidity=all_humidity,  # Add the list of all humidity
        pressure=all_pressure,  # Add the list of all pressure
        weather=all_weather,  # Add the list of all weather
        wind_speed=all_wind_speed,  # Add the list of all wind speed
        wind_dir=all_wind_dir,  # Add the list of all wind direction
        loops=list_len)  # Needed for nicer printing

    return return_data


# Used to display the important information
def print_weather(data, data_type, time_span):
    symbol = '\xb0' + 'F'  # Change to 'C' if Celsius is used
    info = str(data_type).lower()  # Information type required
    return_string = ''  # Final string that will be passed back

    if time_span == 'five_day':
        # Always print the city's name
        return_string += '\nWeather conditions in {} over the past 5 days'.format(data['city'])

        # Opted for if-else statement instead of a dictionary for readability
        if (info == "temp") or (info == "temperature") or (info == "hot") or (info == "cool") or (info == "cold"):
            for entry in range(0, data['loops']):
                return_string += '\n--------------------------------------------------------------------------------'
                return_string += '\nForecast Data Log - Entry {}:'.format(entry+1)
                return_string += '\nTemperature at recording\t\t{}{}'.format(data['temp'][entry], symbol)
                return_string += '\nProjected temperatures\t\t\tHigh {}{}\t\tLow {}{}'.format(
                    data['temp_max'][entry], symbol, data['temp_min'][entry], symbol)

        else:
            # Print information about each entry recorded
            for entry in range(0, data['loops']):
                return_string += '\n--------------------------------------------------------------------------------'
                return_string += '\nForecast Data Log - Entry {}:'.format(entry+1)
                return_string += '\nTemperature at recording\t\t{}{}'.format(data['temp'][entry], symbol)
                return_string += '\nProjected temperatures\t\t\tHigh {}{}\t\tLow {}{}'.format(
                    data['temp_max'][entry], symbol, data['temp_min'][entry], symbol)
                return_string += '\nSky & cloud conditions\t\t\t{} - {}% Coverage'.format(
                    data['weather'][entry], data['cloudiness'][entry])
                return_string += '\nWind speed & angle\t\t\t\tSpeed: {}mph\t\tAngle: {}'.format(
                    data['wind_speed'][entry], data['wind_dir'][entry])
                return_string += '\nHumidity & pressure\t\t\t\tHumidity: {}%\t\tPressure: {}hPa'.format(
                    data['humidity'][entry], data['pressure'][entry])

    else:
        # Always print the city's name
        return_string += '\nCurrent weather in\t\t\t\t{}'.format(data['city'])

        # Opted for if-elif-else statement instead of a dictionary for readability
        if (info == "rain") or (info == "rainy") or (info == "rainfall"):
            return_string += '\nRain in the past three hours\t{}mm'.format(data['rain'])
        elif (info == "snow") or (info == "snowy") or (info == "snowfall"):
            return_string += '\nSnow in the past three hours\t{}mm'.format(data['snow'])
        elif (info == "sky") or (info == "clouds") or (info == "clear") or (info == "weather"):
            return_string += '\nCurrent sky & cloud conditions\t{} - {}% Coverage'.format(
                data['weather'], data['cloudiness'])
        elif (info == "temp") or (info == "temperature") or (info == "hot") or (info == "cool") or (info == "cold"):
            return_string += '\nCurrent temperature\t\t\t\t{}{}'.format(data['temp'], symbol)
            return_string += '\nProjected temperatures\t\t\tHigh {}{}\t\t\tLow {}{}'.format(
                data['temp_max'], symbol, data['temp_min'], symbol)
        else:
            return_string += '\nCurrent temperature\t\t\t\t{}{}'.format(data['temp'], symbol)
            return_string += '\nProjected temperatures\t\t\tHigh {}{}\t\t\tLow {}{}'.format(
                data['temp_max'], symbol, data['temp_min'], symbol)
            return_string += '\nCurrent sky & cloud conditions\t{} - {}% Coverage'.format(
                data['weather'], data['cloudiness'])
            return_string += '\nRain/Snow in past 3 hours\t\tRain: {}mm\t\t\tSnow: {}mm'.format(
                data['rain'], data['snow'])
            return_string += '\nWind speed/angle\t\t\t\tSpeed: {}mph\t\tAngle: {}'.format(
                data['wind_speed'], data['wind_dir'])
            return_string += '\nHumidity/Pressure\t\t\t\tHumidity: {}%\t\tPressure: {}hPa'.format(
                data['humidity'], data['pressure'])
            return_string += '\nSunrise/Sunset times\t\t\tSunrise: {}\tSunset: {}'.format(
                data['sunrise'], data['sunset'])

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
        main_url = url_creator(args['location'], args['time'])  # Assumes arguments are City names
        api_dict = data_collector(main_url)  # Grab base data file

        # Grab data according to which time frame is being used
        if args['time'] == 'five_day':
            api_data = data_organizer_span(api_dict)
        else:
            api_data = data_organizer_current(api_dict)

        final_string = print_weather(api_data, args['weather_type'], args['time'])  # Print information requested

        return final_string

    # I'm not sure what should be done with exceptions now
    except IOError:
        print('Something went wrong with reading data')

# example calls
# print(module_main({'location': 'Philly', 'time': '', 'weather_type': 'temperature'}))
# print(module_main({'location': 'London', 'time': '', 'weather_type': 'rain'}))
# print(module_main({'location': 'Tokyo',  'time': '', 'weather_type': ''}))
# print(module_main({'location': 'Boston', 'time': '', 'weather_type': 'snow'}))

# Example calls 2 - Note that forecast is more limited on data given
# print(module_main({'location': 'New York', 'time': 'five_day', 'weather_type': 'temp'}))
# print(module_main({'location': 'Philly',   'time': 'five_day', 'weather_type': 'weather'}))
# print(module_main({'location': 'London',   'time': 'five_day', 'weather_type': ''}))
