# blueprint_module\page.py
from flask import request, session,render_template, Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors
from . import blueprint

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'seeburgtisch'

# Intialize MySQL
mysql = MySQL(app)

@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    # Output message als er iets fout gaat
    msg = ''
    # Bekijkt of de username en wachtwoord die ingevuld worden echt bestaan
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # Check of het account bestaat in MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # Als het account bestaat
        if account:
            # Maak een session aan (deze session kan je gebruiken in andere routes)
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            msg = 'Logged in successfully!'
            return render_template('index.html', msg=msg)
        else:
            # Het account bestaat niet of username/wachtwoord is verkeerd
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)
