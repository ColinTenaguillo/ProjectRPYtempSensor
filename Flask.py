#!/usr/bin/env python
# -*-coding:Utf-8 -*


"""Flask.py: Test of Flask library"""

from flask import Flask, request, render_template
import pymysql as mdb
app = Flask(__name__)

@app.route('/')
def index():
    con = mdb.connect("localhost", "phpmyadmin", "admin", "phpmyadmin", charset='utf8')
    cur = con.cursor()
    cur.execute('SELECT * FROM Capteurs;')
    results = cur.fetchall()
    print (results)
    return render_template('index.html',templateData=results)

if __name__ == '__main__':
    app.run(host="172.16.3.158",port=5000, debug=True)