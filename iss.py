import turtle
import urllib.request
import json


class Iss:
    def __init__(self, screen):
        self.screen = screen
        self.url = 'http://api.open-notify.org/iss-now.json'

        response = urllib.request.urlopen(self.url)
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
