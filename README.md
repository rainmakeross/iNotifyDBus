iNotifyDBus
===========

Python implementation of iNotify file/directory watcher with dBus messaging (Client/Server).

Once asked to build this for a client and could not find recent tutorials on both libraries (dbus and pyinotify). Took me a while to
go over forums etc. to piece together what needed to be done.

Occurred to me afterwards that this could be useful to the community.

Logic neatly seperated into three files:
dbusClient.py -- Client file for accessing dbusmessenger information.
dbusServer.py -- Server initiating the message service and maintaining.
fileMonitor.py -- pyinotify implementation, it takes command line argument for path to watch, it has recursive and auto-add flags turned on.

Server must be launched first, client second and fileMonitor third.
