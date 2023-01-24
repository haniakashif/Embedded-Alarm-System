#code for pressing of the “*” key:

from gpiozero import Button, LED, Buzzer
from time import sleep

col1 = Button(3)
col2 = Button(21)
col3 = Button(5)
row1 = LED(2)
row2 = LED(7)
row3 = LED(6)
row4 = LED(4)

def star_code():
    row1.on()
    row2.on()
    row3.on()
    row4.off()
    while True:
        if col1.is_pressed:
            print(" * key is pressed")
