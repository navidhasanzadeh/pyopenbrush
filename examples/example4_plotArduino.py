import serial
import time
from openbrush import OpenBrush
import numpy as np

import threading

ob = OpenBrush()

def thread_function():
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=.1)
    time.sleep(0.2)
    ser.read_all()
    c = [6,10]
    while True:
        try:
            b = int(ser.readlines()[-1].strip())
            b = np.min([b, 15])
            c.append(b)            
            color = np.mean(c[-5:])
            color = (color - np.min(c)) / (np.max(c) - np.min(c))
            ob.colorSetRGB([color, 0, 1-color])               
        except:
            pass
        time.sleep(0.1)    


x = threading.Thread(target=thread_function)

x.start()
      

ob.new()

ob.userMoveTo([0,0,20])
ob.brushType("smoke")

x = 0
X = [[0,0,0]] * 20
while True:
    try:
        x = x + 1
        y = 10 * np.sin(x/4)
        z = 10 * np.cos(x/4)        
        X.append([x,y,z])
        ob.drawPaths([X])        
        ob.userMoveTo([-x-10,0,40])
        X = X[1:]
    except:
        pass
    time.sleep(0.05)
