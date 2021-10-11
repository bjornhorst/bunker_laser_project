from flask import Flask, request, redirect, session, render_template, url_for

from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
from routes import blueprint

app = Flask(__name__)
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'key'
# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'seeburgtisch'
app.register_blueprint(blueprint)
#
# # Intialize MySQL
mysql = MySQL(app)
@app.route('/')
def homePage():
    return render_template("index.html")


@app.route('/help')
def helpPage():
    return render_template('help.html')


# THIS ROUTE IS ONLY FOR SHOWING HOW TO PARSE PYTHON TO A TEMPLATE. THIS FILE MUST BE DELETED FOR THE ENDPRODUCT
@app.route('/parsePython')
def parsePythonPage():
    x = 99
    return render_template('parsePython.html', randomNumber=x)


@app.route('/videos')
def videos():
    return render_template('videos.html')


@app.route('/videoCreate')
def createVideos():
    return render_template('videoCreate.html')



@app.route('/logout')
def logout():
    # Verwijderd de session, hierdoor log je uit
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('my_blueprint.login'))


@app.route("/led/on", methods=['POST'])
def move_forward():
    # Moving forward code
    os.system("sudo python scripts/led_on.py")
    forward_message = "Led is on..."
    return render_template('parsePython.html', forward_message=forward_message);


@app.route("/led/off", methods=['POST'])
def move_forward1():
    # Moving forward code
    os.system("sudo python scripts/led_off.py")
    forward_message = "led is off..."
    return render_template('parsePython.html', forward_message=forward_message);


@app.route("/video/on", methods=['POST'])
def move_forward3():
    # Moving forward code
    os.system("sudo python scripts/video_on.py")
    forward_message = "Led is on..."
    return render_template('parsePython.html', forward_message=forward_message);

