#================Heartbeat(push messaging)================
#
# The non-recieved heartbeat limit is 5 beat. 


from typing import Counter, NewType
from Heartbeat import Heartbeat
import time 


i=1 
message=3
index=0
counter=0
flag=False


def HeartbeatMaker1():
    #Exactly 
    time.sleep(1) #heartbeat with 1 second interval 
    return message

def HeartbeatMaker2():
    #Some heartbeats don't send but it is still working. (The function sends 2 none heartbeat)
    global index
    global message
    index+=1
    #print(index)
    time.sleep(1)
    if (index<=3):
        return message
    elif(index>3 and index<=5):
        return None;
    else:
        index=0
        return message;

def HeartbeatMaker3():
    #The function sends 5 none heartbeats.
    global index
    global message
    index+=1
    #print(index)
    time.sleep(1)
    if (index<=3):
        return message
    elif(index>3 and index<=8):
        return None;
    else:
        index=0
        return message;

def HeartbeatMaker4():
    #The function sends message 6 times and none send 6 times.
    global index
    global message
    index+=1
    #print(index)
    time.sleep(1)
    if (index<=6):
        return message
    elif(index>6 and index<=12):
        return None;
    else:
        index=0
        return message;



    
    
while (i<10):
    
    p=Heartbeat(HeartbeatMaker4(),counter,flag)
    text=p.run()
    counter=p.counter
    print("counter=", counter)
    flag=p.flag
    print(text)
    print ("")
