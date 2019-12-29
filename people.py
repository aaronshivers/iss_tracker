import urllib.request
import json


class People:
    def __init__(self):
        url = 'http://api.open-notify.org/astros.json'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print('People in Space:', result['number'])

        people = result['people']

        for p in people:
            print(p['name'], 'in', p['craft'])
