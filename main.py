#!/usr/bin/env python3
"""
System Tray Icon Plugin
Copyright (C) 2013-2020 Lars Windolf <lars.windolf@gmx.de>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject, Gtk
from gi.repository import Gdk, GdkPixbuf

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")

        read_pix = None
        staticon = None
        menu = None
        delete_signal_id = None
        x = None
        y = None

        self.move(0, 0)

        self.do_activate()

    def do_activate(self):
        self.read_pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="emblem-web.svg", width=-1, height=128, preserve_aspect_ratio=True)

        self.staticon = Gtk.StatusIcon ()
        self.staticon.connect("activate", self.trayicon_click)
        self.staticon.connect("popup_menu", self.trayicon_popup)
        self.staticon.set_visible(True)
        self.trayicon_set_pixbuf(self.read_pix)

        self.menu = Gtk.Menu()
        menuitem_toggle = Gtk.MenuItem(label="Show / Hide")
        menuitem_quit = Gtk.MenuItem(label="Quit")

        menuitem_toggle.connect("activate", self.trayicon_toggle)
        menuitem_quit.connect("activate", self.trayicon_quit)
        self.menu.append(menuitem_toggle)
        self.menu.append(menuitem_quit)
        self.menu.show_all()

        self.delete_signal_id = GObject.signal_lookup("delete_event", Gtk.Window)
        GObject.signal_handlers_block_matched (self,
                                               GObject.SignalMatchType.ID | GObject.SignalMatchType.DATA,
                                               self.delete_signal_id, 0, None, None, None)
        self.connect("delete_event", self.trayicon_close_action)
        self.connect("window-state-event", self.window_state_event_cb)

    def window_state_event_cb(self, widget, event):
        "Hide window when minimize"
        if event.changed_mask & event.new_window_state & Gdk.WindowState.ICONIFIED:
            self.deiconify()
            self.save_position()
            self.hide()

    def restore_position(self):
        if self.x != None and self.y != None:
            print("Moving to %d, %d" % (self.x, self.y))
            self.move(self.x, self.y)

    def show_window(self):
        if not self.get_property("visible"):
            self.restore_position()
        self.deiconify()
        self.present()

    def trayicon_click(self, widget, data = None):
        self.show_window()

    def save_position(self):
        self.x, self.y = self.get_position()
        print("Saving position %d, %d" % (self.x, self.y))

    def trayicon_close_action(self, widget, event):
        self.save_position()
        self.hide()
        return True

    def trayicon_toggle(self, widget, data = None):
        if not self.get_property("visible"):
            self.show_window()
        else:
            self.save_position()
            self.hide()

    def trayicon_quit(self, widget, data = None):
        Gtk.main_quit()

    def trayicon_popup(self, widget, button, time, data = None):
        self.menu.popup(None, None, self.staticon.position_menu, self.staticon, 3, time)

    def trayicon_set_pixbuf(self, pix):
        if self.staticon.props.pixbuf != pix:
            self.staticon.props.pixbuf = pix

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
