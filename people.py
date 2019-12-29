import urllib.request
import json


class People:
    def __init__(self):
        self.url = 'http://api.open-notify.org/astros.json'
        self.response = urllib.request.urlopen(self.url)
        self.result = json.loads(self.response.read())

        self.people = self.result['people']

        for p in self.people:
            print(p['name'], 'in', p['craft'])

    def __repr__(self):
        return f'People in Space: {self.people_count()}'

    def people_count(self):
        return self.result['number']