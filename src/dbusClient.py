#!/usr/bin/python
__author__ = 'derya yinanc'

# consumeservice.py
# consumes a method in a service on the dbus



import sys
import traceback

from gi.repository import GLib

import dbus
import dbus.mainloop.glib

def handle_reply(msg):
    """
    >>> handle_reply("test")
    test
    """
    print (msg)

def handle_error(e):
    """
    >>> handle_error("e")
    e
    """
    print (str(e))

def signal_handler(signal):
    """
    >>> signal_handler(["test1","test2"])
    Received signal (by connecting using remote object) and it says: test1:test2
    """
    print ("Received signal (by connecting using remote object) and it says: "
           + signal[0]+":"+signal[1])





# Interpreter runs this if it is ran as an "application"; if methods are being accessed(aka Import)
# ... will not execute this part of the code.

#test method
def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()
    try:
        object  = bus.get_object("com.example.TestService","/com/example/TestService/object")

        object.connect_to_signal("RealSignal", signal_handler, dbus_interface="com.example.TestService", arg0="Hello")
    except dbus.DBusException:
        traceback.print_exc()
        sys.exit(1)

    #lets add a signal receiver
    bus.add_signal_receiver(signal_handler, dbus_interface = "com.example.TestService", signal_name = "RealSignal")




    # Add client to loop
    try:
        loop = GLib.MainLoop()
        loop.run()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise




