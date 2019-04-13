#!/usr/bin/env python
# -*-coding:Utf-8 -*

""".py: Create table for new captor."""

import sys
import pymysql

nom_capteur = str(sys.argv[1])

address = "localhost"
username = "root"
pwd = "root"
database = "Capteurs"

db = pymysql.connect(address, username, pwd, database)
cursor = db.cursor()

sql = (
    f"CREATE TABLE `{nom_capteur}`"
    f"(`id` INT(11) NOT NULL AUTO_INCREMENT,"
    f"`MacAddress` VARCHAR(255), `Temp` INT(10),"
    f"`Hum` INT(10), `Bat` INT(10),"
    f"`Heure` INT(10), PRIMARY KEY(`id`))"
)

try:
    cursor.execute(sql)
    db.commit()
finally:
    db.close()
