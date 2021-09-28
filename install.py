import os
import sys


# if(sys.platform=="win32"):
#     os.system('cmd /k "venv\Scripts\\activate && flask run"')
# elif(sys.platform=="linux" or sys.platform =="linux2"):
#     os.system("source env/bin/activate")
#     os.system("flask run")

if(sys.platform=="win32"):
    os.system('cmd /c python -m venv venv && "venv\Scripts\\activate"')
    #os.system('cmd /c "venv\Scripts\\activate"')
    #os.system('cmd /c pip install flask')
    # os.system('cmd /c python install flask-mysqldb')

