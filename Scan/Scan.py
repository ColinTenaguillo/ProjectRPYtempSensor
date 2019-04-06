#!/usr/bin/env python
# -*-coding:Utf-8 -*

from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import mef
from threading import Timer

def change_i():
    global i #required to address globally declared variables
    i = 1

Externe = "d7:ef:13:27:15:29" #Mac adress of the sensor
Interne = "d6:c6:c7:39:a2:e8"

#Note this must be run as root!
i = 1
while True :   # here we make a bluetooth scan, maybe a function would be more appropriate but it works
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

    scanner = Scanner().withDelegate(ScanDelegate()) #just scan
    devices = scanner.scan(10.0) #give all scanning data to devices
    mef.ecriturescansql(Externe,devices) #writing data of the Externe sensor
    mef.ecriturescansql(Interne,devices) #writing data of the Interne sensor
    t = Timer(10.0, change_i)
    if (i == 1):
        mef.ecriturescansql_histo(Externe, devices)
        mef.ecriturescansql_histo(Interne, devices)
        i = 0
        print(i)
        t.start()