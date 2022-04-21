import os
import sys


if(sys.platform=="win32"):
    os.system('cmd /k "venv\Scripts\\activate && flask run"')
elif(sys.platform=="linux" or sys.platform =="linux2"):
    os.system("source venv/bin/activate")
    os.system("flask run")