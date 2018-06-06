from gpiozero import Button
from gpiozero import LED
from time import sleep

def button_is_pressed():
    sensor = Button(2)
    return sensor.is_pressed
        
def ledd():
    led = LED(17)
    led.off()
    while 1 == 1:
            led.on()
            sleep(10)
            led.off()

if __name__ == '__main__':
    while True:
        print('main')
