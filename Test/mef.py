#!/usr/bin/env python
# -*-coding:Utf-8 -*

"""mef.py: Fonctions"""

import pymysql

def ecriturescansql(macadress,devices) :
    for dev in devices:
        if dev.addr in macadress :
            db = pymysql.connect("localhost", "phpmyadmin", "admin", "phpmyadmin")
            cursor = db.cursor()
            for (adtype, desc, value) in dev.getScanData():
                if len(value) == 38 :
                    Temperature = int(value[24:28], 16) / 100
                    Humidite = int(value[28:32], 16) / 100
                    Battery = int(value[20:22], 16)
                    sql = "UPDATE `Capteurs` SET `Temp`=" + str(Temperature) + ",`Hum`=" + str(Humidite) + ",`Batt`=" + str(Battery) + " WHERE `ID` = '" + macadress + "'"
                    print(sql)
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
            db.close()