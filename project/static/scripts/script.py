import os
import sys
import os, sys, signal
import time
import csv
pid=os.getpid ()
print("HIJ WERKT NU NOG")
with open ('pid.csv','w') as csvfile:
    wr=csv.writer(csvfile)
    wr.writerow ( [ 'WORK1',pid])
while (True):
    print ('Programmatic Trading')
    time.sleep (1)
print("This process has the PID", os.getpid())
# while True:
#     for i in range(10000):
#         sys.stdout.write('\r')
#         sys.stdout.write(str(i))
#         sys.stdout.flush()
