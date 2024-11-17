from machine import Pin
from hcsr04 import HCSR04
from time import sleep

sensor= HCSR04(trigger_pin=5,echo_pin=22, echo_timeout_us=1000000)

tank_d=15
while True:
    distance=sensor.distance_cm()
    print(distance,'cm')
    if distance>3 and distance<=15:
        per=100-((100/tank_d)*distance)
        print("Water Level:",per,"%")
    elif distance<=3:
        print("Tank full")
    else:
        print("Tank Empty!!")
    sleep(2)