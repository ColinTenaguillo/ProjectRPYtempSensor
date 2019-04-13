#!/usr/bin/env python
# -*-coding:Utf-8 -*

""".py: Create table for new captor"""

import sys
import pymysql  # library for phpmysql

nom_capteur = str(sys.argv[1])

address = "localhost"
username = "root"
pwd = "root"
database = "Capteurs"

db = pymysql.connect(address, username, pwd, database)  # Connecting the the DB
cursor = db.cursor()  # Variable that we will use to write in the DB

sql = (
    "CREATE TABLE `" + nom_capteur + "`"
    "(\
    `id` INT(11) NOT NULL AUTO_INCREMENT,\
    `MacAddress` VARCHAR(255),\
    `Temp` INT(10),\
    `Hum` INT(10),\
    `Bat` INT(10),\
    `Heure` INT(10),\
    PRIMARY KEY(`id`)\
)"
)

try:
    cursor.execute(sql)  # launch the command
    db.commit()  # commit changes
except:
    db.rollback()  # if error, rollback
db.close()  # disconnect from DB
