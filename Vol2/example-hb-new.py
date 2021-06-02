import time
message=3
timeout = 300
timeout_start = time.time()
def HeartbeatMaker(a,b):
    global message
    global timeout
    a = int(a)
    b = int(b)
    if(time.time() < timeout_start + a):
         time.sleep(1)
         return message
    elif(time.time()<=timeout_start + a+b):
        time.sleep(1)
        return None
    else:
        time.sleep(1)
        return message

while time.time() < timeout_start + timeout:
    pp=HeartbeatMaker(5,5)
    print(pp)
