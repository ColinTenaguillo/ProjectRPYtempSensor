#!/usr/bin/env python
# -*-coding:Utf-8 -*


"""Flask.py: Test of Flask library"""

from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="172.16.3.158",port=5000)