#!/usr/bin/python
__author__ = 'derya yinanc'



from gi.repository import GLib
import dbus
import dbus.service
import dbus.mainloop.glib
import sys
import traceback





class TestObject(dbus.service.Object):
    def __init__(self, conn, object_path='/com/example/TestService/object'):
        dbus.service.Object.__init__(self, conn, object_path)


    @dbus.service.signal('com.example.TestService')
    def RealSignal(self, message):
        pass


    @dbus.service.method('com.example.TestService')
    def emitRealSignal(self, message):
        self.RealSignal(message)
        return 'Signal emitted'

    @dbus.service.method("com.example.TestService",
                         in_signature='', out_signature='')
    def Exit(self):
        loop.quit()

# Interpreter runs this if it is ran as an "application"; if methods are being accessed(aka Import)
# ... will not execute this part of the code.
if __name__ == '__main__':


    try:
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        session_bus = dbus.SessionBus()
        name = dbus.service.BusName('com.example.TestService', session_bus)
        object = TestObject(session_bus)
    except dbus.DBusException:
        traceback.print_exc()
        sys.exit(1)


    #add Server to loop
    try:
        loop = GLib.MainLoop()
        print ("Running example signal emitter service.")
        loop.run()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise






