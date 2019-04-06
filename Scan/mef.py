#!/usr/bin/env python
# -*-coding:Utf-8 -*

"""mef.py: Functions"""

import pymysql #library for mysql

address = "localhost"
username = "root"
pwd = "root"
database = "Capteurs"

#We admit that in the .py we call this function a scandelegate with bluepy has been done
#Function that will translate and write data we received from the bluetooth temperature sensor in the PhpMysql DB
def ecriturescansql(macadress,devices) : #define the function with 2 arguments
    for dev in devices: #basic loop for all the devices
        if dev.addr in macadress : #dev.addr = bluetooth devices   variable macadress is given when we call the function
            db = pymysql.connect(address, username, pwd, database) #Connecting the the DB
            cursor = db.cursor() #Variable that we will use to write in the DB
            for (adtype, desc, value) in dev.getScanData(): #Loop for all data
                if len(value) == 38 : #Selecting the good raw data of our temperature sensor(value 38 depending on the sensor)
                    Temperature = int(value[24:28], 16) / 100 #temperature data is between 24:28 and put it in decimal, we divide per 100 cause of the comma
                    Humidite = int(value[28:32], 16) / 100 #Same for Humidity
                    Battery = int(value[20:22], 16) #Same for battery
                    sql = "UPDATE `Capteurs` SET `Temp`=" + str(Temperature)\
                          + ",`Hum`=" + str(Humidite) + ",`Batt`=" + str(Battery)\
                          + " WHERE `ID` = '" + macadress + "'" #sql bash command we want to use
                    try:
                        cursor.execute(sql) #launch the command
                        db.commit() #commit changes
                    except:
                        db.rollback() #if error, rollback
            db.close() #disconnect from DB

def ecriturescansql_histo(macadress,devices) :
    for dev in devices:  # basic loop for all the devices
        if dev.addr in macadress:  # dev.addr = bluetooth devices   variable macadress is given when we call the function
            db = pymysql.connect(address, username, pwd, database)  # Connecting the the DB
            cursor = db.cursor()  # Variable that we will use to write in the DB
            for (adtype, desc, value) in dev.getScanData():  # Loop for all data
                if len(value) == 38:  # Selecting the good raw data of our temperature sensor(value 38 depending on the sensor)
                    Temperature = int(value[24:28], 16) / 100  # temperature data is between 24:28 and put it in decimal, we divide per 100 cause of the comma
                    Humidite = int(value[28:32], 16) / 100  # Same for Humidity
                    Battery = int(value[20:22], 16)  # Same for battery
                    sql = "UPDATE `Capteurs_Histo` SET `Temp`=" + str(Temperature)\
                          + ",`Hum`=" + str(Humidite) + ",`Batt`=" + str(Battery)\
                          + " WHERE `ID` = '" + macadress + "'"  # sql bash command we want to use
                    try:
                        cursor.execute(sql)  # launch the command
                        db.commit()  # commit changes
                    except:
                        db.rollback()  # if error, rollback
            db.close()  # disconnect from DB

