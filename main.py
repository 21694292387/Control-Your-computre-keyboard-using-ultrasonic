import serial  # open terminal write pip3 or pip in mac . pip install pyserial mean python serial
import time
import pyautogui # the something

picoSerial = serial.Serial('/dev/cu.usbmodem14101', 9600) # 9600 baudrate means receive byte per second ./dev/... usb name in mindows or linux not the something im windows com3 com2 com9
time.sleep(4)

while 1: # 1 mean true
    incoming = str(picoSerial.readline())  # read the serial data and print it as line
    print(incoming) # print incoming data

    if 'Pause/Play' in incoming: # if condition
        pyautogui.typewrite(['space'], 0.2) # python auto guide press space in keyboard
              

    incoming = "";

