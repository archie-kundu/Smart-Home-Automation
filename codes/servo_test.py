from machine import Pin, PWM
from servo import Servo
from time import sleep

motor=Servo(pin=13)

while True:
    for i in range(0,91,10):
        motor.move(i)
        sleep(0.5)
    sleep(3)
    for i in range(91,0,-10):
        motor.move(i)
        sleep(0.5)
    sleep(1)


