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
@blueprint.route('/register', methods=['GET', 'POST'])
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

