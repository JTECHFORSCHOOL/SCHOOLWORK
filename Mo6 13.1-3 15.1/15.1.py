import multiprocessing
from time import sleep
import random
from datetime import datetime

def counter():
    sleep(random.uniform(0,1))
    currentDate = datetime.now()
    strDate = currentDate.strftime("%d %B %Y")
    print(strDate)

if __name__=='__main__':
    for i in range(3):
        p = multiprocessing.process(target=counter, args ="strDate")

    p.start()
