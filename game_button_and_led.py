from gpiozero import Button
from gpiozero import LED
from time import sleep

def button_is_pressed():
    sensor = Button(2)
    return sensor.is_pressed
        
def ledd():
    led = LED(17)
    led.off()
    led.on()
    sleep(.1)
    led.off()

if __name__ == '__main__':
    while True:
        print('main')
