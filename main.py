import json
import urllib.request
import turtle
import time

from settings import Settings
from location import Location


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
        houston = Location(29.5502, -95.097)
        independence = Location(39.091118, -94.415504)
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
