#!/usr/bin/env python
# -*-coding:Utf-8 -*

"""mef.py: Functions."""


import pymysql
import itertools
import datetime

address = "localhost"
username = "root"
pwd = "root"
database = "Capteurs"


def insertintocapteurs(macadress, devices):
    """Insert dans la BD Capteurs."""
    for dev in devices:
        if dev.addr in macadress:
            db = pymysql.connect(address, username, pwd, database)

            cursor = db.cursor()
            for (_adtype, _desc, value) in dev.getScanData():
                if len(value) == 38:
                    temperature = str(int(value[24:28], 16) / 100)
                    humidite = str(int(value[28:32], 16) / 100)
                    battery = str(int(value[20:22], 16))
                    sql = (
                        f"INSERT INTO `{macadress}`"
                        f"(MacAddress,Temp,Hum,Bat,Heure) "
                        f"VALUES (`{macadress}`,`{temperature}`,"
                        f"`{humidite}`,`{battery}`,`{heureminute()}`);"
                    )

                    try:
                        cursor.execute(sql)
                        db.commit()
                    finally:
                        db.close()


def recupnomtables():
    """Get name of the tables in DB Capteurs."""
    db = pymysql.connect(address, username, pwd, database)
    cursor = db.cursor()
    sql = "SHOW TABLES"
    cursor.execute(sql)
    results_tuple = cursor.fetchall()  # return list of tuple
    results_array = list(itertools.chain.from_iterable(results_tuple))
    for result in results_array:
        result.replace("'", "")
        result.replace("',)", "")
    db.close()
    return results_array


def heureminute():
    """Get local hour and minute."""
    date = datetime.datetime.now()
    heuremin = date.time().strftime("%H.%M")
    return heuremin
