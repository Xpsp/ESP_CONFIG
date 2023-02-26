from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)

while True:
    led.on() #  led.value(1)
    sleep_ms(500) # delay of 500 ms
    led.off() # led.value(0)
    sleep_ms(500) # delay of 500 ms