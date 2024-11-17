'''
3.3v to 3v
GND to GND
RST to GPIO 4
SDA TO GPIO 5
SCK TO GPIO 18
MISO TO GPIO 19
MOSI TO GPIO 23

Servo: Pin 13
'''


from time import sleep
from mfrc522 import MFRC522
from machine import Pin, PWM
from machine import SPI
from servo import Servo

spi = SPI(2, baudrate=2500000, polarity=0, phase=0)

spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
print("Place card")

led = Pin(2,Pin.OUT)
data = []
c=0
while True:
    
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print(card_id)
            
            if card_id == "uid: 0x23c9a2fd":
                print('Door Open')
                led.value(1)
                sleep(0.5)
                led.value(0) 
                motor=Servo(pin=13)
                for i in range(0,91,10):
                    motor.move(i)
                    sleep(0.5)
                sleep(3)
                for i in range(91,0,-10):
                    motor.move(i)
                    sleep(0.5)
                sleep(1)
                led.value(1)
                sleep(0.5)
                led.value(0)                
            else:
                c+=1
                print('Door Locked')
                led.value(0)
                if(c==5):
                    print("Security Alert")
                    led.value(1)
                    sleep(10)
                    led.value(0)
                    c=0
                    
            
            
