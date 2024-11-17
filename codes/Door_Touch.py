from machine import Pin
from time import sleep
import con
import ufirebase as firebase

URL='http://smart-home-automation-b7375-default-rtdb.firebaseio.com/'

x = Pin(4,Pin.IN)
Data={}
Data2={}
while True:
    y = x.value()
    print(y)
    sleep(0.4)
    firebase.put(URL,'doorbell')
#     Data2 = Data['Smart Home Automation' ]
#     print(Data)
#     dataup=Data2['doorbell']
#     print(dataup)
    
    

    