import turtle
import urllib.request
import json

class People:
    def __init__(self, screen):
        self.screen = screen

        url = 'http://api.open-notify.org/astros.json'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print('People in Space:', result['number'])

        people = result['people']

        for p in people:
            print(p['name'], 'in', p['craft'])

        url = 'http://api.open-notify.org/iss-now.json'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        location = result['iss_position']
        lat = float(location['latitude'])
        lon = float(location['longitude'])
        print('Latitude:', lat)
        print('Longitude:', lon)

        self.screen.register_shape('iss2.gif')
        iss = turtle.Turtle()
        iss.shape('iss2.gif')
        iss.setheading(90)

        iss.penup()
        iss.goto(lon, lat)