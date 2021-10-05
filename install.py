import os
import sys
import subprocess

# if(sys.platform=="win32"):
#     os.system('cmd /k "venv\Scripts\\activate && flask run"')
# elif(sys.platform=="linux" or sys.platform =="linux2"):
#     os.system("source env/bin/activate")
#     os.system("flask run")

if (sys.platform == "win32"):
    import subprocess

    # This command could have multiple commands separated by a new line \n
    # some_command = "cmd /c ping www.google.com"
    some_command = "python -m venv venv && venv\Scripts\\activate && py -m pip install flask && py -m pip install flask-mysqldb && pip install python-dotenv"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    print(output)


