import con
from machine import Pin, ADC
from time import sleep
import dht
from hcsr04 import HCSR04
import ufirebase as firebase

while True:
    
    #LPG Detection
    gas = ADC(34)
    buz = Pin(2,Pin.OUT)
    tv = 2500
    gas_value = gas.read()
    print(gas_value)
    if (gas_value>tv):
      buz.value (1)
    else:
      buz.value(0)
    sleep(0.2)
      

    #Temperature Control
    dht_pin_number = 21  
    dht_sensor = dht.DHT11(Pin(dht_pin_number))
    threshold_temp = 26
    led = Pin(26,Pin.OUT)
    
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        if (temperature >threshold_temp):
            led.value(1)
        else:
            led.value(0)
    except Exception as e:
        pass
    sleep(0.2)
    
    
    #Water Level in Tank
    sensor= HCSR04(trigger_pin=5,echo_pin=25, echo_timeout_us=1000000)
    tank_d=7
    distance=sensor.distance_cm()
    print(distance,'cm')
    if distance>3 and distance<=tank_d:
        per=100-((100/tank_d)*distance)
        print("Water Level:",per,"%")
    elif distance<=3:
        print("Tank full")
    else:
        print("Tank Empty!!")
    sleep(0.2)
    
    #Door Lock
    lock = Pin(15,Pin.IN)
    print(lock.value())
    sleep(0.2)
    
    #Door Bell
    bell = Pin(23,Pin.IN)
    print(bell.value())
    sleep(0.2)
    
    print("\n")
    
    
    
