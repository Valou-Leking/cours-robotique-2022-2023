from machine import Pin      
import time 

Motion_Detected = False 

def handle_interrupt(Pin):          
    global Motion_Detected
    Motion_Detected = True

led=Pin(2,Pin.OUT)   
PIR_Interrupt=Pin(3,Pin.IN)   

PIR_Interrupt.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)        

i = 0

while True:
   time.sleep_ms(100)
   print(i)
   if Motion_Detected:
       led.value(1)
       if i == 2:
           i = 0
       else:
          i = i + 1
       Motion_Detected = False
   else:
       led.value(0) 
   