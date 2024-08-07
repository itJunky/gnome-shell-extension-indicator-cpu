import os
import psutil
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import GLib, Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

APPINDICATOR_ID = 'myappindicator'
CURRPATH = os.path.dirname(__file__)

refresh_time = 500

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
        notify.init(APPINDICATOR_ID)
        self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
        print(f'end of init: {self.indicator.get_icon()}')


    def build_menu(self):
        menu = gtk.Menu()
        item_color = gtk.MenuItem(label='Sun')
        item_color.connect('activate', self.change_sun)

        item_color2 = gtk.MenuItem(label='Gray')
        item_color2.connect('activate', self.change_rain)

        item_quit = gtk.MenuItem(label='Exit')
        item_quit.connect('activate', self.quit)

        menu.append(item_color)
        menu.append(item_color2)
        menu.append(item_quit)
        menu.show_all()
        return menu


    def change_sun(self, source):
        self.indicator.set_icon_full(CURRPATH+"/summer-rain-svgrepo-com.svg", '123')

    def change_rain(self, source):
        self.indicator.set_icon_full(CURRPATH+"/cloud-svgrepo-com.svg", '321')

    def check_cpu_load(self):
        cpu_load = psutil.cpu_percent()
        print(cpu_load)
        if cpu_load < 10:
            self.indicator.set_icon_full(CURRPATH+"/10_prcnt.svg", 'CPU: 10%')
        if 20 > cpu_load > 10:
            self.indicator.set_icon_full(CURRPATH+"/20_prcnt.svg", 'CPU: 20%')
        if 30 > cpu_load > 20:
            self.indicator.set_icon_full(CURRPATH+"/30_prcnt.svg", 'CPU: 30%')
        if 40 > cpu_load > 30:
            self.indicator.set_icon_full(CURRPATH+"/40_prcnt.svg", 'CPU: 40%')
        if 50 > cpu_load > 40:
            self.indicator.set_icon_full(CURRPATH+"/50_prcnt_green.svg", 'CPU: 50%')
        if 60 > cpu_load > 50:
            self.indicator.set_icon_full(CURRPATH+"/60_prcnt_yellow.svg", 'CPU: 60%')
        if 70 > cpu_load > 60:
            self.indicator.set_icon_full(CURRPATH+"/70_prcnt_yellow.svg", 'CPU: 70%')
        if 80 > cpu_load > 70:
            self.indicator.set_icon_full(CURRPATH+"/80_prcnt_orange.svg", 'CPU: 80%')
        if 90 > cpu_load > 80:
            self.indicator.set_icon_full(CURRPATH+"/90_prcnt_orange.svg", 'CPU: 90%')
        if 100 > cpu_load > 90:
            self.indicator.set_icon_full(CURRPATH+"/100_prcnt_red.svg", 'CPU: 100%')
        menu = gtk.Menu()
        menu.show_all()

    def quit(self, source):
        gtk.main_quit()

    def on_timeout(self, data):
        print('InnerLoop')
        self.check_cpu_load()
        self.timeout_id = GLib.timeout_add(refresh_time, self.on_timeout, None)


def main():
    #indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'whatever', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    #indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    #indicator.set_menu(gtk.Menu())
    ind = Indicator()
    gtk.main()
    ind.main_loop()
    print('gtk main ended')

if __name__ == "__main__":
    main()
