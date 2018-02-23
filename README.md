# flask_platform

There are three modules in flask_platform.
__init__.py initialize the package
views.py  import flask
          import 
          create an instance of Flask class called app
          route to tell Flask what URL to trigger funciton
          
running.py import views
           main run the flask function on localhost:5000 when __name__ == __main__
           flaskrun run the flask function on localhost:5000
         
modify the setup.py, set entry_points as flask_platform.running:flaskrun,

So when enter the command flask_platform in command line after installing the falsk_platform package, system will execute the function flaskrun in running module.
