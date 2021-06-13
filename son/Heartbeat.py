import queue
from time import time, sleep
import multiprocessing



treshold=5
timeout_start = time()
#monitoring heartbeat
class Monitor:
    def __init__(self, q1):
        self.q1=q1
    def run(self):
        flag=False
        message=3 
        
        while(True==True):
            
            value=self.q1.get()
            if(flag==False):
                if value!=message and value!=None:
                    print("message missmatch")
                elif value==None:
                    
                    a=time()
                    while(value ==None):
                        print("Status=OK2")
                        value=self.q1.get()
                        b=time()
                        if(treshold<(b-a)):
                            flag=True
                            sleep(1)
                            print("Error=The function is not working.")
                            break
                        
                elif value == message:
                    print("Status=OK")
                else:
                    print("unknown error")
                    
            elif(flag==True):
                if value!=message and value!=None:
                    print("message missmatch")
                elif value == message:
                    a=time()
                    while(value == message):
                        value=self.q1.get()
                        b=time()   
                        print("Error=The function is not working")
                        if(treshold<(b-a)):
                            print("Status changed=OK")
                            flag=False
                            break

                elif value==None:
                    print("Error=The function is not working.")

                else:
                    print("unknown error")


#heartbeat creator        
class Heartbeat_Maker:
    def __init__(self,q,a,b):
        
        self.a=a #true signal count
        self.b=b #false signal count
        self.q=q #sended signal
    def run(self):
        message=3
        timeout_start=time()
        while(True==True): 
            sleep(1)
            elapsed=(time()-timeout_start)   
            if(elapsed<self.a):
                
                self.q.put(message)

            elif(elapsed>self.a and elapsed<self.b+self.a):
                self.q.put(None)
            else:
                timeout_start=time()
                self.q.put(message)
                
            #print(self.q.get())
            
        
            
            


                    
                




            

        
       
            
        
       
            
