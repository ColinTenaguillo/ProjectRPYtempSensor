#!/usr/bin/env python
# -*-coding:Utf-8 -*

from bluepy.btle import Scanner, DefaultDelegate, Peripheral


demo = "d7:ef:13:27:15:29"
demo2 = "d6:c6:c7:39:a2:e8"

while True :
   class ScanDelegate(DefaultDelegate):
       def __init__(self):
           DefaultDelegate.__init__(self)

   scanner = Scanner().withDelegate(ScanDelegate())
   devices = scanner.scan(10.0)


   for dev in devices:
       if dev.addr == demo :
           for (adtype, desc, value) in dev.getScanData():
               if len(value) == 38 :
                    Batteryext = int(value[20:22], 16)
                    Températureext = int(value[24:28], 16) / 100
                    Humiditéext = int(value[28:32], 16) / 100
                    print("Extérieur - ")
                    print("Batterie : " + str(Batteryext)+ "%")
                    print("Température : " + str(Températureext) + " degrès" )
                    print("Humidité " + str(Humiditéext) + " % ")
       if dev.addr == demo2 :
           for (adtype, desc, value) in dev.getScanData():
               if len(value) == 38 :
                    Batteryint = int(value[20:22], 16)
                    Températureint = int(value[24:28], 16) / 100
                    Humiditéint = int(value[28:32], 16) / 100
                    print("Intérieur - ")
                    print(" Batterie :  " + str(Batteryint) + "%")
                    print(" Température : " + str(Températureint) + " degrès")
                    print("Humidité : " + str(Humiditéint) + " %")
           break
