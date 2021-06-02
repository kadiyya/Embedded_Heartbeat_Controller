
from typing import Counter, NewType
from Heartbeat import Monitor, Heartbeat_Maker
import time 
import multiprocessing

message=3
counter=0
flag=False


if __name__ == "__main__":

    # creating multiprocessing Queue
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=Heartbeat_Maker(), args=(..........))
    p2 = multiprocessing.Process(target=Monitor(), args=(q, ))


    #starting processes
    p1.start()
    p2.start()