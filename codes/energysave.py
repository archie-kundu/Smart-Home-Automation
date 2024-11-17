from machine import Pin
from time import sleep

ir1 = Pin(23, Pin.IN)
ir2 = Pin(22, Pin.IN)
led = Pin(15, Pin.OUT)

flag1 = False
flag2 = False
c=0
while True:
    d1 = ir1.value()
    d2 = ir2.value()
    print(d1,d2)
    if d1 == 0 and d2 == 1 and flag2 == False:
        flag1 = True
    elif flag1 == True:
        if d1 == 1 and d2 == 0:
            c+=1
            flag1 = False
    
    elif d1 == 1 and d2 == 0 and flag1 == False:
        flag2 = True
    elif flag2 == True:
        if d1 == 0 and d2 == 1:
            c-=1
            flag2 = False
    print(flag1, flag2)
    if c > 0:
        led.value(1)
    else:
        led.value(0)
        
    print("Number of Persons:",c)
    sleep(0.5)
