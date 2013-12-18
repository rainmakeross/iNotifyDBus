#!/usr/bin/python
__author__ = 'derya yinanc'

import pyinotify
import traceback
import sys
import dbus
import dbus.service
import argparse


bus = dbus.SessionBus()
try:
    object  = bus.get_object("com.example.TestService","/com/example/TestService/object")
except dbus.DBusException:
    traceback.print_exc()
    sys.exit(1)
# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.ALL_EVENTS
#mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_ATTRIB | pyinotify.IN_DELETE_SELF \
#       | pyinotify.IN_MODIFY | pyinotify.IN_MOVE_SELF | pyinotify.IN_MODIFY | pyinotify.IN_CLOSE_WRITE# watched events


def sendSignal(message):
    object.emitRealSignal(message, dbus_interface="com.example.TestService")

class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        message="Creating:", event.pathname
        print ("Creating:", event.pathname)
        sendSignal(message)


    def process_IN_CREATE(self, event):
        message="Creating:", event.pathname
        print ("Creating:", event.pathname)
        sendSignal(message)

    def process_IN_DELETE(self, event):
        message="Removing:", event.pathname
        print ("Removing:", event.pathname)
        sendSignal(message)

    def process_IN_ATTRIB(self, event):
        message="Metadata Changed:", event.pathname
        print ("Metadata Changed:", event.pathname)
        sendSignal(message)

    def process_IN_DELETE_SELF(self, event):
        message="Watched Directory Deleted:", event.pathname
        print ("Watched Directory Deleted:", event.pathname)
        sendSignal(message)

    def process_IN_MODIFY(self, event):
        message="Modified:", event.pathname
        print ("Modified:", event.pathname)
        sendSignal(message)

    def process_IN_MOVED_FROM(self, event):
        message="Moved From:", event.pathname
        print ("Moved From:", event.pathname)
        sendSignal(message)

    def process_IN_MOVED_TO(self, event):
        message="Moved To:", event.pathname
        print ("Moved To:",  event.pathname)
        sendSignal(message)







# Interpreter runs this if it is ran as an "application"; if methods are being accessed(aka Import)
# ... will not execute this part of the code.
if __name__ == '__main__':
    #Command line argument handling
    parser = argparse.ArgumentParser(description='This is a demo script by Derya Yinanc.')
    parser.add_argument('-p','--path',help='Path', required=True)


    args = parser.parse_args()
    path = args.path


    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)


    wdd = wm.add_watch(path, mask, rec=True, auto_add=True, proc_fun=handler)

    notifier.loop()