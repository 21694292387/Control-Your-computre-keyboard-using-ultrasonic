from machine import Pin
import utime 
trig = Pin(1,Pin.OUT)
ech = Pin(0 , Pin.IN)
def mesure():
    trig.low()
    utime.sleep_us(2)
    trig.high() 
    utime.sleep(5)
    trig.low()
    while ech.value() == 0 :
        signaloff = utime.ticks_us()
    while ech.value() == 1 :
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343)/2  
    print("distance from object is : ",str(distance)+" " +"cm")
    if distance < 20 :
        prinr("Pause/Play")
    
while True :
    mesure() 
    utime.sleep(0.3)