

import json
import urllib.request
import urllib.parse
import datetime

request = input('What is your location right now? ')

raw_answer = urllib.request.urlopen('http://transport.opendata.ch/v1/stationboard?station=' + urllib.parse.quote(request, safe='') + '&limit=10')

answer = json.load(raw_answer)

print('Your location was found: ' + answer['station']['name'])

connections = answer['stationboard']
for connection in connections:
    name = connection['name']
    category = connection['category']
    to = connection['to']
    departure_time = datetime.datetime.strptime(connection['stop']['departure'][:-5], '%Y-%m-%dT%H:%M:%S')
    in_minutes = int((departure_time - datetime.datetime.now()).total_seconds() / 60)
    print(category + '(' + name + ')' + ' runs in ' + str(in_minutes) + ' Minutes to ' + to)

