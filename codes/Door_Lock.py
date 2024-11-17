from machine import Pin
from time import sleep

led = Pin(15,Pin.IN)
while True:
    print (led.value())
    sleep(1)