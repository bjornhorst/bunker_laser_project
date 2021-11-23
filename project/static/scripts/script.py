import os
import time
import csv
import sys

def getPID():
    pid = os.getpid()
    print("HIJ WERKT NU NOG")
    with open('pid.csv', 'w') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['WORK1', pid])
    print("This process has the PID", os.getpid())
    # latest_tutorial.py
    # from reader import feed

def main(start):

    a = [[3, True], [6, False], [15, True], [20, False], [35, True], [50, False], [120, False]]
    i = 0
    while True:
        time1 = a[i][0]
        end = time.perf_counter() + start
        if (end >= time1):
            print(a[i][1])
            print(end)
            i += 1
if __name__ == "__main__":
    getPID()
    test = sys.argv[1]
    # test = test[0]
    print(test)
    main(float(test))