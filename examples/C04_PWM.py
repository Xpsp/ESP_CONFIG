from machine import Pin, PWM

pwm2 = PWM(Pin(2), freq=60, duty=512)
print(pwm2)