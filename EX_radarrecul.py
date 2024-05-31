from machine import Pin, time_pulse_us
import time

SOUND_SPEED = 340  # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US = 10

trig_pin = Pin(15, Pin.OUT)  
echo_pin = Pin(14, Pin.IN)  
led_pin = Pin(17, Pin.OUT)   
buzzer_pin = Pin(22, Pin.OUT) 

while True:
    # Prépare le signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) 
    distance_cm = SOUND_SPEED * ultrason_duration / 20000  

    print(f"Distance : {distance_cm} cm") 

    if distance_cm < 10: 
        led_pin.value(1)  
        buzzer_pin.value(1) 
    else:
        led_pin.value(0) 
        buzzer_pin.value(0) 

    time.sleep_ms(500) 
