#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from flask_platform import views
from flask_platform.views import app



def flaskrun():
    app.run(host='0.0.0.0',port=5000)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)