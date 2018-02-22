#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from flask_platform.views import setapp
from flask_platform.views import setroute


app=setapp("src/flask_platform/templates")
setroute(app)
app.run(host='0.0.0.0',port=5006)