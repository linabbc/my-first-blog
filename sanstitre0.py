# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:06:16 2020

@author: 33664
"""
from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World!"








if __name__ == "__main__" and "get_ipython" not in locals():  # ne pas exécuter dans un notebook
    app.run()