# !/usr/bin/env python
# -*-coding:Utf-8 -*

"""ScanCaptorDB.py: Scan and write in the tables."""


# Note this must be run as root

from bluepy.btle import Scanner, DefaultDelegate
import mef


class ScanDelegate(DefaultDelegate):
    """Scan for bluetooth devices."""

    def __init__(self):
        DefaultDelegate.__init__(self)


while True:
    scanner = Scanner().withDelegate(ScanDelegate())  # just scan
    devices = scanner.scan(10.0)
    tables = mef.recupnomtables()
    for table in tables:
        mef.insertintocapteurs(table, devices)
