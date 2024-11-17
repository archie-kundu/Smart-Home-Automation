#Donot Remove or Add to PIN 21

import time
from machine import Pin
import dht

# Define the DHT11 sensor pin
dht_pin_number = 21  # Replace with your GPIO pin number
dht_sensor = dht.DHT11(Pin(dht_pin_number))
threshold_temp = 26
led = Pin(15,Pin.OUT)

while True:
    try:
        # Read temperature and humidity
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        # Print the results
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        if (temperature >threshold_temp):
            led.value(1)
        else:
            led.value(0)
    except Exception as e:
        print(f"Error: {e}")

    # Delay for a few seconds before the next reading
    time.sleep(2)
    
led.value(0)