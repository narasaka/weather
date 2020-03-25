import requests
from apikeys import ipstack_key

page1 = requests.get('https://ipinfo.io')
value1 = page1.json()
value1Co = value1['loc']
value1CoList = value1Co.split(',')
value1Lat = float(value1CoList[0])
value1Lng = float(value1CoList[1])

apiUrl2 = 'https://freegeoip.app/json/'
page3 = requests.get(apiUrl2)
value3 = page3.json()
value3Lat = value3['latitude']
value3Lng = value3['longitude']

try:
    apiUrl1 = 'http://api.ipstack.com/check?access_key=' + ipstack_key
    page2 = requests.get(apiUrl1)
    value2 = page2.json()
    value2Lat = value2['latitude']
    value2Lng = value2['longitude']
except Exception:
    latAvg = (value1Lat + value3Lat)/2
    lngAvg = (value1Lng + value3Lng)/2

latAvg = str((value1Lat + value2Lat + value3Lat)/3)
lngAvg = str((value1Lng + value2Lng + value3Lng)/3)
