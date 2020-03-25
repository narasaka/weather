from forecast import Forecast
from currentLocation import latAvg, lngAvg
from apikeys import darksky_key
from datetime import datetime
from geopy.geocoders import Nominatim
import os
import sys

fc = Forecast(latAvg, lngAvg, darksky_key)

def currentFc():
    print(datetime.fromtimestamp(fc.time).strftime('%Y-%m-%d %H:%M:%S'))
    print(fc.timezone)

    os.chdir('./resources')

    if fc.icon == 'clear-day':
        with open('sun.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'clear-night':
        with open('moon.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'rain':
        with open('cloud-rain.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'snow':
        with open('snowflake.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'wind':
        with open('snowflake.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'fog':
        with open('cloud.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'cloudy':
        with open('cloud.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'partly-cloudy-day':
        with open('cloud.txt', 'r') as f:
            print(f.read())
    elif fc.icon == 'partly-cloudy-night':
        with open('cloud.txt', 'r') as f:
            print(f.read())

    print(fc.currentSummary())
    print(str(fc.temperature) + ' °C')
    print('Feels like ' + str(fc.apparentTemperature) + ' °C')
    print('Chance of rain is ' + str(fc.precipProbability) + '%')

def quick():
    print(fc.currentSummary())

def advice():
    print('Still in development. Sorry!')


try:
    arg = sys.argv[1]
except IndexError:
    currentFc()
else:
    try:
        location = ' '.join(sys.argv[2:])

        if arg == '-h' or arg == '--help':
            print('\nFormatting command:')
            print('weather [option] [location]\n')
            print('The [option] is optional.')
            print('You may leave it blank and go with the forecast based on your ip address.')
            print('The [location] can be just a city, or your full address.\n')
            print('-----\n')
            print('example 1(no option): weather')
            print('example 2(with -h option): weather -h (displays guide/help page)')
            print('example 3(with find feature): weather -f seattle(displays forecast for Seattle)\n')
            print('-----\n')
            print('option list:')
            print('-a or --advice: display an advice #still in development, sorry lol')
            print('-f or --find: set mode to "find" and lets you input [location]')
            print('-h or --help: display guide/help page.')
            print('-q or --quick: display a one-sentence weather summary')
            print('-v or --version: display current version program.')

        elif arg == '-v' or arg == '--version':
            print('\nv0.0.2beta(narasaka) powered by DarkSky')

        elif arg == '-q' or arg == '--quick':
            quick()

        elif arg == '-a' or arg == '--advice':
            advice()

        elif arg == '-f' or arg == '--find':
            geo = Nominatim(user_agent='weather')
            loc = geo.geocode(location)
            fc = Forecast(str(loc.latitude), str(loc.longitude), darksky_key)
            currentFc()

        else:
            print('\ncommand not found. try "weather -h" to display guide.')

    except Exception:
        print('Error 404. Location not found.')
