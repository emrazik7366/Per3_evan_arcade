from gpiozero import Button
from time import sleep
from Per3_evan_arcade import arcade_final_code
def buttonn():
    sensor = Button(2)
    while 1 == 1:
        sensor.wait_for_press()
        sleep(.5)
def ledd():
    led = LED(17)
    led.off()
    while 1 == 1:
        if self.game_over == True:
            led.on()

if __name__ == '__main__':
    while True:
        print('main')
