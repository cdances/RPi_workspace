#!/usr/bin/python 
# Blink Demo
# Derived from http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html
#

# Problem Parameters
PIN=11
BLINKS=100
BLINK_ON=0.050
BLINK_OFF=0.050

Banner=""""Blink Demo
Writing to pin: {0:}
Number of Blinks: {1:}
Blinks Time ON: {2:} sec
Blinks Time OFF: {3:} sec
Expected run time: {4:} sec
Using 2, 270 Ohm Resistors to drop voltage before reaching LED
DO NOT STOP THIS WHILE PROGRAM IS RUNNING!!!
""".format(PIN,BLINKS,BLINK_ON,BLINK_OFF,BLINKS*(BLINK_ON+BLINK_OFF))

print Banner

import RPi.GPIO as GPIO  
import time  

# blinking function  
def blink(pin,on_time,off_time):
	# Should maybe have a try and/or catch exception here???
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(on_time)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(off_time)  
        return  

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(PIN, GPIO.OUT)  
# blink GPIO17 50 times  
for i in range(0,BLINKS):  
        blink(PIN,BLINK_ON,BLINK_OFF)  
GPIO.cleanup()


