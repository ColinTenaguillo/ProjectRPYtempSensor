#!/usr/bin/env python
# -*-coding:Utf-8 -*

""".py: Create table for new captor"""

import sys
import pymysql #library for phpmysql

nom_capteur = sys.argv[1]

address = "localhost"
username = "root"
pwd = "root"
database = "Capteurs"

db = pymysql.connect(address, username, pwd, database) #Connecting the the DB
cursor = db.cursor() #Variable that we will use to write in the DB

sql = "CREATE TABLE" + nom_capteur +\
"(\
    id INT PRIMARY KEY NOT NULL,\
    nom VARCHAR(100),\
    MacAddress VARCHAR(100),\
    Temp INT,\
    Hum INT,\
    Bat INT,\
    Heure INT,\
)"

try:
    cursor.execute(sql) #launch the command
    db.commit() #commit changes
except:
    db.rollback() #if error, rollback
db.close() #disconnect from DB