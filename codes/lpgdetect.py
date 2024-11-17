from machine import Pin, ADC
from time import sleep

gas = ADC(34)
buz = Pin(2,Pin.OUT)
tv = 2500

while True:
  gas_value = gas.read()
  print(gas_value)
  if (gas_value>tv):
      buz.value (1)
  else:
      buz.value(0)
  sleep(0.5) 