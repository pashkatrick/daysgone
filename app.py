import rumps
from datetime import date
import datetime


class LifeApp(object):
    def __init__(self):
        self.config = {
            'app_name': 'Days Gone',
            'init': 'Get Days'
        }
        self.app = rumps.App(self.config['app_name'])
        self.app.title = '🍅'
        self.start_init_button = rumps.MenuItem(
            title=self.config['init'], callback=self.days_gone)
        self.app.menu = [self.start_init_button]

    def days_gone(self, sender):
        # fix that to custom
        d0 = date(0000, 00, 00)
        d1 = datetime.datetime.now().date()
        delta = d1 - d0
        result = str(round(delta.days/365, 3))
        self.app.title = f'you lived for {result} days'

    def run(self):
        self.app.run()


# TODO
# - get birth date
# - auto update number every day


if __name__ == '__main__':
    app = LifeApp()
    app.run()
