from machine import Pin, UART, PWM, ADC # importe tous les types de pines que nous avons besoin
import time

ENA = PWM(Pin(0)) # défini IN1 comme étant une sortie PWM( modulation de la largeur d'impultion ) sur la pin 0
ENA.freq(2000)

IN1 = Pin(1, Pin.OUT) # défini IN1 comme étant une sortie numérique sur la pin 1 
IN2 = Pin(2, Pin.OUT)
Vrx = ADC(Pin(26)) # défini Vrx comme étant une entrée analogique sur la pine 26
Vry = ADC(Pin(27))

def scale_value (value,in_min,in_max,out_min,out_max): # Est une fonction qui traduit les valeurs de sortie du joystique en un pourcentage.
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 
    return scaled_value

while True:
    val_y = Vrx.read_u16() # variable, val_y correspond à la valeur du joystique recu sur la pine Vry. 
    val_x = Vry.read_u16()
    print(val_y)
    time.sleep_ms(200) # pour avoir le temps de lire la valeur sur val_y

    if val_y <= 45000:
        ENA.duty_u16(val_y) # applique la valeur analogique de val_y sur la sortie PWM relié à la carte .
        IN1.value(1) # pines qui définices le sens de rotation du moteur vers l'avant, relié au module L298N
        IN2.value(0) 
        print(int(scale_value(y_value,0,45000,0,100))) # écrit le pourcentage auquel le moteur tourne , en utilisant la fonction scale_value

    elif val_y >= 55000:
        ENA.duty_u16(val_y) # applique la valeur analogique de val_y sur la sortie PWM relié à la carte .
        IN1.value(0) # pines qui définices le sens de rotation du moteur vers l'avant, relié au module L298N
        IN2.value(1)
        print(int(scale_value(y_value,50000,65535,0,100))) # écrit le pourcentage auquel le moteur tourne , en utilisant la fonction scale_value
        
    else:
        IN1.value(0) # pines qui définices le sens de rotation du moteur (ici ne troune pas) , relié au module L298N
        IN2.value(0)