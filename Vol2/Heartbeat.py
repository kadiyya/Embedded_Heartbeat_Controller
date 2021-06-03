import time
import multiprocessing
message=3
treshold=5
timeout = 300
timeout_start = time.time()
q = multiprocessing.Queue()
class Monitor:
    def __init__(self, q):
        self.recieved=q
        #Flag is used for when connection broke, the program wait for threshold number succesive heartbeat
    def run(self):
        
        
        if self.recieved == message:
            print("Status=OK")
        elif self.recieved==None:
           
            time1=process_time()
            while(self.recieved != message):
                time2=process_time()
                if(treshold<(time2-time1)):
                    print("The function is not working.")

class Heartbeat_Maker:
    def __init__(self, q):
        self.send=q
        
    def Heartbeat_Maker(a,b):
        
        global timeout
        a = int(a)
        b = int(b)
        if(time.time() < timeout_start + a):
            time.sleep(1)
            q.put (message)
        elif(time.time()<=timeout_start + a+b):
            time.sleep(1)
            q.put (None)
        else:
            time.sleep(1)
            q.put (message)

    while time.time() < timeout_start + timeout:
        pp=Heartbeat_Maker(5,5)
        print(pp)
                    
                




            

        
       
            
        
       
            
