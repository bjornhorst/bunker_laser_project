import os
import sys
import subprocess

if (sys.platform == "win32"):
    #some_command = "python -m venv venv && venv\Scripts\\activate && py -m pip install flask && py -m pip install flask-mysqldb && pip install python-dotenv"
    some_command = "python -m venv venv && venv\Scripts\\activate && py -m pip install flask python-dotenv flask-sqlalchemy flask-login flask-mail pyjwt dotenv flask-wtf"

    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    print(output)
elif(sys.platform=="linux" or sys.platform =="linux2"):
    os.system("python3 -m venv venv && venv/bin/activate && py -m pip install flask && py -m pip install flask-mysqldb && pip install python-dotenv")

