import turtle
import time
import urllib.request
import json


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        location = turtle.Turtle()
        location.penup()
        location.color('yellow')
        location.goto(self.longitude, self.latitude)
        location.dot(5)
        location.hideturtle()

        url = 'http://api.open-notify.org/iss-pass.json'
        url = url + '?lat=' + str(self.latitude) + '&lon=' + str(self.longitude)
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        over = result['response'][1]['risetime']

        # print over
        style = ('Arial', 6, 'bold')
        location.write(time.ctime(over), font=style)