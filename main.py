import turtle

from settings import Settings
from location import Location
from people import People
from iss import Iss


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
        self.get_iss()
        houston = Location(29.5502, -95.097)
        independence = Location(39.091118, -94.415504)
        while True:
            self._update_screen()

    def _update_screen(self):
        self.screen.update()

    @staticmethod
    def get_people():
        people = People()
        print(people)

    def get_iss(self):
        Iss(self.screen)


if __name__ == '__main__':
    iss_tracker = IssTracker()
    iss_tracker.run_iss_tracker()
