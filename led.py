from gpiozero import LED
from time import sleep

light = LED(17)

on = int(input("time on "))
off = int(input("time off "))

def blinker(on, off):
    while True:
        light.on()
        sleep(on)
        light.off()
        sleep(off)

blinker(on, off)
