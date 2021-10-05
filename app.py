from flask import Flask, request, redirect, session, render_template, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
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

# Intialize MySQL
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


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     # Output message als er iets fout gaat
#     msg = ''
#     # Bekijkt of de username en wachtwoord die ingevuld worden echt bestaan
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         # Check of het account bestaat in MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
#         # Fetch one record and return result
#         account = cursor.fetchone()
#         # Als het account bestaat
#         if account:
#             # Maak een session aan (deze session kan je gebruiken in andere routes)
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             # Redirect to home page
#             msg = 'Logged in successfully!'
#             return render_template('index.html', msg=msg)
#         else:
#             # Het account bestaat niet of username/wachtwoord is verkeerd
#             msg = 'Incorrect username/password!'
#     # Show the login form with message (if any)
#     return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    # Bekijkt of username, password en email echt zijn ingevuld
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # Als het account al bestaat laat error zien en validatie
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Als het account nog niet bestaat en de waardes zijn goed, voer onderstaande query uit
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('register.html', msg=msg)
    elif request.method == 'POST':
        # Formulier is leeg
        msg = 'Please fill out the form!'
    # Laat het register formulier opnieuw zien
    return render_template('register.html', msg=msg)


@app.route('/uploader', methods=['POST'])
def uploader():
    file = request.files['inputFile']
    name = request.form['videoName']
    BinaryData = file.read()

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""INSERT INTO videos (name, data)"""
                   """VALUES (%s, %s)""",
                   (name, BinaryData))
    mysql.connection.commit()

    return render_template('index.html')


@app.route('/logout')
def logout():
    # Verwijderd de session, hierdoor log je uit
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))


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

