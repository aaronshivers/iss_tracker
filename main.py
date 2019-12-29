import json
import urllib.request
import turtle
import time

from settings import Settings


class IssTracker:
    def __init__(self):
        self.settings = Settings()

        self.screen = turtle.Screen()
        self.screen.setup(self.settings.screen_width, self.settings.screen_height)
        self.screen.bgpic(self.settings.screen_bgpic)
        self.screen.setworldcoordinates(
            self.settings.screen_llx,
            self.settings.screen_lly,
            self.settings.screen_urx,
            self.settings.screen_ury
        )

    def run_iss_tracker(self):
        self.get_people()
        while True:
            self._update_screen()

    def _update_screen(self):
        self.screen.update()

    def get_people(self):
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


if __name__ == '__main__':
    iss_tracker = IssTracker()
    iss_tracker.run_iss_tracker()

# url = 'http://api.open-notify.org/astros.json'
# response = urllib.request.urlopen(url)
# result = json.loads(response.read())
# print('People in Space:', result['number'])
#
# people = result['people']
#
# for p in people:
#     print(p['name'], 'in', p['craft'])
#
# url = 'http://api.open-notify.org/iss-now.json'
# response = urllib.request.urlopen(url)
# result = json.loads(response.read())
#
# location = result['iss_position']
# lat = float(location['latitude'])
# lon = float(location['longitude'])
# print('Latitude:', lat)
# print('Longitude:', lon)

# screen = turtle.Screen()
# screen.setup(720, 360)
# screen.setworldcoordinates(-180, -90, 180, 90)
# screen.bgpic('map.gif')

# screen.register_shape('iss2.gif')
# iss = turtle.Turtle()
# iss.shape('iss2.gif')
# iss.setheading(90)
#
# iss.penup()
# iss.goto(lon, lat)

# space center, Huston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']

# print over
style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

# Independence, MO
lat = 39.091118
lon = -94.415504

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']

# print over
style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)
