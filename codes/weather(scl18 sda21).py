import con
import urequests
import time

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?lat=22.571870190911607&lon=88.37140765745805&appid=af786b16ba952de2c0e7e3ef755ac358&units=metric'

i2c = SoftI2C(scl=Pin(18), sda=Pin(21), freq=1000000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

def get_weather_data():
    try:
        response = urequests.get(BASE_URL)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching weather data:", e)
        return None

def display_weather(weather_data):
    if weather_data:
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        

        return description,temp
    else:
        return None

def display_suggestion(weather_description):
    suggestion = ""
    if "rain" in weather_description.lower():
        suggestion = "Take an Unbrella!"
    
    elif "mist" in weather_description.lower():
        suggestion = "Dress Warmly & Reduced Visibility!"
    
    elif "haze" in weather_description.lower():
        suggestion = "Stay Indoor, Reduced Visibilty!"
        
    elif "snow" in weather_description.lower():
        suggestion = "Dress Warmly!"

    elif "cloud" in weather_description.lower():
        suggestion = "It's a Cloudy Day!"

    else:
        suggestion = "Enjoy the Weather!"
    
    return suggestion


# Main loop
while True:
    lcd.clear()
    try:
        weather_data = get_weather_data()
        w_d,t = display_weather(weather_data)
        print(t)

        if w_d:
            x = display_suggestion(w_d)
        
        degree = bytearray([0x06,0x09,0x09,0x06,0x00,0x00,0x00,0x00])
        lcd.custom_char(0, degree)
        lcd.putstr("Temp   : "+str(t)+chr(0)+"C")
        lcd.putstr("Climate: "+str(w_d)[0].upper()+str(w_d)[1::])
        time.sleep(5)
        lcd.clear()
        for i in range(0,totalColumns):
            x=" "+x
        x=x+"  "
        
        for i in range(0,len(x)):
            lcd.move_to(0,0)
            lcd.putstr(str(x)[i:(i+totalColumns):])
            time.sleep(0.6)

        time.sleep(0.5)
    except:
        pass
