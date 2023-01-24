#(h) code for keypad:

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
            print("enter password")
            password()

def main():
    star_code()

def password():
    code='126725'
    password=''
    while True:
        sleep(1)
        if len(password)==6:
            break
        while True:
            row1.on()
            row2.on()
            row3.on()
            row4.off()
            if col1.is_pressed:
                print('*', end='')
                password+='*'
                break
            elif col2.is_pressed:
                print('0', end='')
                password+='0'
                break
            elif col3.is_pressed:
                print('#', end='')
                password+='#'
                break
            row1.on()
            row2.on()
            row3.off()
            row4.on()
            if col1.is_pressed:
                print('7', end='')
                password+='7'
                break
            elif col2.is_pressed:
                print('8', end='')
                password+='8'
                break
            elif col3.is_pressed:
                print('9', end='')
                password+='9'
                break
            row1.on()
            row2.off()
            row3.on()
            row4.on()
            if col1.is_pressed:
                print('4', end='')
                password+='4'
                break
            elif col2.is_pressed:
                print('5', end='')
                password+='5'
                break
            elif col3.is_pressed:
                print('6', end='')
                password+='6'
                break
            row1.off()
            row2.on()
            row3.on()
            row4.on()
            if col1.is_pressed:
                print('1', end='')
                password+='1'
                break
            elif col2.is_pressed:
                print('2', end='')
                password+='2'
                break
            elif col3.is_pressed:
                print('3', end='')
                password+='3'
                break
           
    if password==code:
        print('\n'+'Mubarak Ho!!!')
    else:
        print('\n'+'wrong')
        star_code()
    
main()
