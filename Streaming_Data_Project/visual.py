import serial
import numpy
import  matplotlib.pyplot as plt
from drawnow import *
import time

dist=[]

data = serial.Serial("/dev/ttyACM0",9600)
plt.ion() #tell matplotlib you want interactive mode to plot live data

def makeFig():
    plt.plot(dist,'ro-')

while(True):
    
    if(data.inWaiting()>0):
        
        mydata=data.readline()
        mydata=str(mydata)
        distance=float(mydata[2:len(mydata)-5])
        dist.append(distance)
        drawnow(makeFig)
        plt.pause(.000001)
        if (len(dist)>50):
            dist.pop(0)
       