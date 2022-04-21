import os,signal
import pandas as pd
pid=pd.read_csv('pid.csv', names=['prog', 'pid'])
x=0
if (pid['prog'] [x]=='WORK1'):
    os.kill (pid['pid'] [x],signal.SIGTERM)