#!/usr/bin/env python
# -*-coding:Utf-8 -*

from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import mef

Externe = "d7:ef:13:27:15:29" #Mac adress of the sensor
Interne = "d6:c6:c7:39:a2:e8"

#Note this must be run as root!

while True :   # here we make a bluetooth scan, maybe a function would be more appropriate but it works
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

    print("Scanning...") #not usefull but help me to know where i am
    scanner = Scanner().withDelegate(ScanDelegate()) #just scan
    devices = scanner.scan(10.0) #give all scanning data to devices

    print("Scan fini début de modifications de la table")  #not usefull but help me to know where i am
    print("Externe") #not usefull but help me to know where i am
    mef.ecriturescansql(Externe,devices) #writing data of the Externe sensor
    print("Interne") #not usefull but help me to know where i am
    mef.ecriturescansql(Interne,devices) #writing data of the Interne sensor
