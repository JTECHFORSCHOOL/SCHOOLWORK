import multiprocessing
import time
import random
from datetime import datetime

def counter():
    print("triggered")
    sleepTime = random.random()
    time.sleep(sleepTime)
    currentDate = datetime.now()
    strDate = currentDate.strftime("%d %B %Y")
    print(strDate)

if __name__=='__main__':
    for i in range(3):
        p = multiprocessing.Process(target=counter)
        p.start()
