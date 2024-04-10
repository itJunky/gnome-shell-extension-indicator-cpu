import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

APPINDICATOR_ID = 'myappindicator'
#CURRPATH = os.path.dirname(os.path.relpath(__file__))
CURRPATH = os.path.dirname(__file__)

print(f'file: {__file__}')
print(f'relpath: {os.path.relpath(__file__)}')
print(f'dirname: {os.path.dirname(__file__)}')


class Indicator():
    def __init__(self):
        self.indicator = appindicator.Indicator.new(
                        APPINDICATOR_ID, 
                        CURRPATH+"/summer-rain-svgrepo-com.svg",
                        appindicator.IndicatorCategory.SYSTEM_SERVICES
        )
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        print('menu builded')
        print(CURRPATH)
        notify.init(APPINDICATOR_ID)
        print(f'end of init: {self.indicator.get_icon()}')

    def build_menu(self):
        menu = gtk.Menu()
        print('here1')
        item_color = gtk.MenuItem(label='Change 1')
        item_color.connect('activate', self.change_sun)

        item_color2 = gtk.MenuItem(label='Change 2')
        item_color2.connect('activate', self.change_rain)

        menu.append(item_color)
        menu.append(item_color2)
        print('here2')
        menu.show_all()
        print('menu showed')
        return menu


    def change_sun(self, source):
        print(CURRPATH)
        print(dir(self.indicator))
        self.indicator.set_icon_full(CURRPATH+"/summer-rain-svgrepo-com.svg", '123')

    def change_rain(self, source):
        print(dir(self.indicator))
        menu = gtk.Menu()
        self.indicator.set_icon_full(CURRPATH+"/cloud-snow-alt-svgrepo-com.svg", '321')
        menu.show_all()

    def quit(self, source):
        gtk.main_quit()


def main():
    #indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'whatever', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    #indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    #indicator.set_menu(gtk.Menu())
    Indicator()
    print('main indicator init')
    #print(dir(gtk))
    gtk.main()
    print('gtk main')

if __name__ == "__main__":
    main()
