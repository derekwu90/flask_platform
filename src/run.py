import os
from flask_platform import views
from flask_platform.views import app

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)