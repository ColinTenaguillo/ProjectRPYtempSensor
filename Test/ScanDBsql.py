#!/usr/bin/env python
# -*-coding:Utf-8 -*


""".py: Scan BT avec insertion dans bdd PhpMysql"""

#!/usr/bin/env python
# -*-coding:Utf-8 -*

from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import pymysql

Externe = "d7:ef:13:27:15:29"
Interne = "d6:c6:c7:39:a2:e8"

while True :
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

    print("Scanning...")
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)

    print("Scan fini début de modifications de la table")
    for dev in devices:
        if dev.addr == Externe :
            db = pymysql.connect("localhost", "phpmyadmin", "admin", "phpmyadmin")
            cursor = db.cursor()
            for (adtype, desc, value) in dev.getScanData():
                if len(value) == 38 :
                    Temperatureext = int(value[24:28], 16) / 100
                    Humiditeext = int(value[28:32], 16) / 100
                    Batteryext = int(value[20:22], 16)
                    sql1 = "UPDATE `Capteurs` SET `Temp`=" + str(Temperatureext) + ",`Hum`=" + str(Humiditeext) + ",`Batt`=" + str(Batteryext) + " WHERE `ID` = 1"
                    print(sql1)
                    try:
                        cursor.execute(sql1)
                        db.commit()
                    except:
                        db.rollback()
            db.close()
        if dev.addr == Interne :
            db = pymysql.connect("localhost", "phpmyadmin", "admin", "phpmyadmin")
            cursor = db.cursor()
            for (adtype, desc, value) in dev.getScanData():
                if len(value) == 38 :
                    Temperatureint = int(value[24:28], 16) / 100
                    Humiditeint = int(value[28:32], 16) / 100
                    Batteryint = int(value[20:22], 16)
                    sql2 = "UPDATE `Capteurs` SET `Temp`=" + str(Temperatureint) + ",`Hum`=" + str(Humiditeint) + ",`Batt`=" + str(Batteryint) + " WHERE `ID` = 2"
                    print(sql2)
                    try:
                        cursor.execute(sql2)
                        db.commit()
                    except:
                        db.rollback()
            db.close()
