#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
import sysinfo

from flask import Flask


app = Flask(__name__)



@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'WU DI'
    returnDict['info'] = sysinfo.get_platform_info()
    return render_template("index.html", **returnDict)