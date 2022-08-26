from machine import Pin
import utime 
trig = Pin(1,Pin.OUT)
ech = Pin(0 , Pin.IN)
def mesure():
    trig.low()
    utime.sleep_us(2)
    trig.high() # or we can write trig.value(1) 1 mean high // 0 mean low
    utime.sleep(5)
    trig.low()
    while ech.value() == 0 :
        signaloff = utime.ticks_us()
    while ech.value() == 1 :
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343)/2 # speed of sound 343 metre per seconde (local parfait) /2 5atrr 7sebna L wa9t mta3 aller w retoure 
    print("distance from object is : ",str(distance)+" " +"cm")
    
while True :
    mesure() # call function
    utime.sleep(0.3) # lezm n7otou sleep time eli howa delay bech ikoun L mesure mta3 distance bien precis
    # lahnee fi shell matla3li chay 5atr manich 7at L capteur nchallh live jey na3Lm L cablage w betbi3a bech nzidou faza wa9tli tkoun
    #distance a9al mn 20 L pc yenzl espace wala ya3ml ayy 7aja T7bha nty
    
    



