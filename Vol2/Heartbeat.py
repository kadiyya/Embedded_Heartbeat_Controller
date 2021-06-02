from time import process_time, sleep

message=3
treshold=5
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
                    
                




            

        
       
            
        
       
            
