from apikeys import darksky_key
import requests
import os


class Forecast:

    def __init__(self, latitude, longitude, api_key):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key

        url = 'https://api.darksky.net/forecast/'
        response = requests.get(url+self.api_key+'/'+self.latitude+','+self.longitude+'?units=auto&exclude=alerts,flags')

        self.current = response.json()['currently']
        try:
            self.minutely = response.json()['minutely']
        except Exception:
            pass
        self.timezone = response.json()['timezone']
        self.time = self.current['time']
        self.icon = self.current['icon']
        self.temperature = self.current['temperature']
        self.apparentTemperature = self.current['apparentTemperature']
        self.precipProbability = self.current['precipProbability']*100

    def currentSummary(self):
        return self.current['summary']

    def minutelySummary(self):
        return self.minutely['summary']

class Art:

    def __init__(self):
        pass
