import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

start = time.time()
print(start)
a = [[3, True],[6, False], [15,True], [20,False], [35, True], [50,False]]
i = 0
while True:
    time1 = a[i][0]
    end = time.time()
    duration = end-start
    if(duration >= time1):
        GPIO.output(18, a[i][1])
        print(a[i][1])
        print(end)
        print(duration,"sec")
        i += 1






