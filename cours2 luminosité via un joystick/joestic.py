from machine import Pin,UART
from machine import Pin,PWM
from machine import ADC, Pin
import time

SW = Pin(2 , Pin.IN, Pin.PULL_UP)
adc = ADC(Pin(26))
adc2 = ADC(Pin(27))
pwm = PWM(Pin(0))
pwm.freq(2000)

while True:
    print(SW.value())
    y_value = adc.read_u16()
    x_value = adc2.read_u16()
    print("la valeur en Y est:", y_value)
    print("la valeur en X est:", x_value)
    pwm.duty_u16(y_value)
    time.sleep_ms(200)
