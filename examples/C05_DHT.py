from machine import Pin
from time import sleep
import dht

dht11 = dht.DHT11(Pin(4))

while True:
    dht11.measure()
    temp = dht11.temperature()
    humi = dht11.humidity()
    print(temp, humi)
    sleep(1)