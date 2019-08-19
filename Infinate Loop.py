import time
import random
count = random.randint(1,100)
count1= random.randint(1,10)
count2= random.randint(1,10)
count3= random.randint(1,10)
count4= random.randint(1,10)
count5= random.randint(1,10)
while count < 9999999999999:
    count += count1
    countr= round(count,2)
    print(countr)
    time.sleep(0.5)
    count -= count2
    countr= round(count,2)
    print(countr)
    time.sleep(0.5)
    count *= count3
    countr= round(count,2)
    print(countr)
    time.sleep(0.5)
    count /= count4
    countr= round(count,2)
    print(countr)
    time.sleep(0.5)
    count *= count5
    countr= round(count,2)
    print(countr)
    time.sleep(0.5)
