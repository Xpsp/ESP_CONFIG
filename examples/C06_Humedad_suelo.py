from machine import ADC, Pin
from time import sleep

sensor_air = 600
sensor_water = 308

adc = ADC(Pin(13))
adc.atten(ADC.ATTN_6DB)
adc.width(ADC.WIDTH_10BIT)

def linear_conversion(x, x1, x2, y1, y2):
    y = (y2-y1)/(x2-x1)*(x-x1)+y1
    return y

while True:
    lecture = adc.read()     # return lecture in bits 0-2^10-1 i.e 0 - 1023
    #conversion = linear_conversion(lecture, 0, 1023, 0, 100)
    conversion = linear_conversion(lecture, 600, 300, 0, 100)
    print(lecture, round(conversion,2))    
    sleep(0.1)