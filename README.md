# Laser project
### First run only (for installation)

**Installation Windows**

* First create an environment:
  
    `python -m venv venv`


* After that activate the environment:

    `venv\Scripts\activate`
* if you get this error:
  
    `cannot be loaded because the execution of scripts is disabled on this system.`
    
    open powershell as admin and use this command
  
  `Set-ExecutionPolicy RemoteSigned`

**Installation MacOs and linux**

* First create an environment:

    `python3 -m venv venv`
* After that activate the environment:

    `source venv/bin/activate`

**After you created the virtual environment you need to install the packages inside the environment useing the following command**
 
`python setup.py install`

### After installation u can use:
  `python start.py` to run the program






