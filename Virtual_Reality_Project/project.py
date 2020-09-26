import serial
from vpython import *
import time
data = serial.Serial("/dev/ttyACM0",9600)
#measuring = cylinder(length=6,color=color.yellow,radius=.5,pos=vector(-3,-2,0))
Label=label(text="target Distqnce : ",pos = vector(0,10,0),height=30,box=False,color=color.white)
target=box(color=color.green,length=.2,width=10,height=5,pos=vector(-6,0,0))
mybox=box(color=color.blue,length=.1,width=10,height=5,pos=vector(-8.5,0,0))
Tube1=cylinder(color=color.white,pos=vector(-8.5,0,2.5),radius=1.5,length=2.5,thickness=0.1)
Tube2=cylinder(color=color.white,pos=vector(-8.5,0,-2.5),radius=1.5,length=2.5,thickness=0.1)
#cyrcle1=shapes.circle(pos=[-2,0],radius=1.3,thickness=1,rotate=90)
#cyrcle2=shapes.circle(pos=[-2,0],radius=1.3,thickness=1,rotate=90)

while(True):
    rate(20)
    if(data.inWaiting()>0):
        
        mydata=data.readline()
        mydata=str(mydata)
        distance=float(mydata[2:len(mydata)-5])
        #measuring.length=distance
        target.pos=vector(distance-6,0,0)
        myLabel= "Target Distance : " + str(distance)
        Label.text = myLabel

        print(myLabel)
