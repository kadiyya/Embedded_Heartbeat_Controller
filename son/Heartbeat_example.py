from Heartbeat import Monitor 
from Heartbeat import Heartbeat_Maker
import time
import multiprocessing
import queue




True_Message=6 #count of true message 
None_Message=5 #count of false message
q = multiprocessing.Queue()
if __name__ == "__main__":

    po=Heartbeat_Maker(q,True_Message,None_Message)
    pq=Monitor(q)

    #creating multiprocessing 
    t2 = multiprocessing.Process(target=pq.run)
    t1 = multiprocessing.Process(target=po.run)
    
    #starting
    t2.start()
    t1.start()
    
    t1.join()
    t2.join()

    
    