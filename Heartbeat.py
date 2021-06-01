import time

message=3
treshold=5
class Heartbeat:
    def __init__(self, recieved, counter, flag):
        self.recieved=recieved
        self.counter=counter
        self.flag=flag
        #Flag is used for when connection broke, the program wait for threshold number succesive heartbeat
    def run(self):
        
        print("recieved parameter=",self.recieved)
            
        
        if self.flag==False:
            if treshold<=self.counter:
                self.counter=0
                self.flag=True
                return "The microcontroller is not working."
            
            if self.recieved==None:
                self.counter+=1
                return "status=ok"
            elif(self.recieved==message):
                self.counter=0
                return "status=ok"
            else:
                return "missmatch occured"
        elif self.flag==True:   
           
            if treshold<=self.counter:
                self.counter=0
                self.flag=False
                return "The microcontroller started to work."
            
            if self.recieved==None:
                self.counter=0
                return "The microcontroller is not working."
            elif(self.recieved==message):
                self.counter+=1
                return "The microcontroller is not working."
            else:
                return "missmatch occured"
        