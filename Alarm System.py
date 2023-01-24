#(i) Code for the entire alarm system:

from gpiozero import Button, LED, Buzzer, DistanceSensor
from signal import pause
from time import sleep


def buzzer_(buzzer):
    buzzer.beep(on_time=.5, off_time = .5, n = None, background = True)

def check_star():
    row1.on()
    row2.on()
    row3.on()
    row4.off()
    while True:
        if col1.is_pressed:
            return True


def passwords(password):
    password = ""
    while col1.is_pressed or col2.is_pressed or col3.is_pressed:
        pass
    while True:
       
            row1.on()
            row2.on()
            row3.on()
            row4.off()
           
            if col1.is_pressed:
                print('*', end='')
                password+='*'
                while col1.is_pressed:
                    pass
               
            elif col2.is_pressed:
                print('0', end='')
                password+='0'
                while col2.is_pressed:
                    pass
               
            elif col3.is_pressed:
                print('#', end='')
                password+='#'
                while col3.is_pressed:
                    pass
               
            row1.on()
            row2.on()
            row3.off()
            row4.on()
            if col1.is_pressed:
                print('7', end='')
                password+='7'
                while col1.is_pressed:
                    pass
               
            elif col2.is_pressed:
                print('8', end='')
                password+='8'
                while col2.is_pressed:
                    pass
               
            elif col3.is_pressed:
                print('9', end='')
                password+='9'
                while col3.is_pressed:
                    pass
               
            row1.on()
            row2.off()
            row3.on()
            row4.on()
            if col1.is_pressed:
                print('4', end='')
                password+='4'
                while col1.is_pressed:
                    pass
               
            elif col2.is_pressed:
                print('5', end='')
                password+='5'
                while col2.is_pressed:
                    pass
               
            elif col3.is_pressed:
                print('6', end='')
                password+='6'
                while col3.is_pressed:
                    pass
               
            row1.off()
            row2.on()
            row3.on()
            row4.on()
            if col1.is_pressed:
                print('1', end='')
                password+='1'
                while col1.is_pressed:
                    pass
               
            elif col2.is_pressed:
                print('2', end='')
                password+='2'
                while col2.is_pressed:
                    pass
               
            elif col3.is_pressed:
                print('3', end='')
                password+='3'
                while col3.is_pressed:
                    pass
            if len(password) == 4:
                return password

       
def check_code(password, correct):
    if password == correct:
        return True
    else:
        return False
   
def check_distance(threshold):
    while True:
        print(sensor.distance)
        if sensor.distance <= threshold:
            buzzer_(buzzer)
            red.on()
            return True
        else:
            blue.on()
            return False

def main():

    global alarm, col1, col2, col3, row1, row2, row3, row4, light, sensor, buzzer, red, green , blue

    col1 = Button(27)
    col2 = Button(22)
    col3 = Button(10)
    row1 = LED(2)
    row2 = LED(3)
    row3 = LED(4)
    row4 = LED(17)
    buzzer = Buzzer(14)
    red = LED(15)
    blue= LED(23)
    green=LED(18)
    sensor = DistanceSensor(echo = 24, trigger = 25)
    buzzer.off()
    password = ''
    correct = '1234'
    #check_star()
    disabled=True
    while True:
        if disabled and check_star():
                print ('Enter code to enable system')
                password = passwords(password)
                if check_code(password, correct):
                    print('enabled')
                    red.off()
                    blue.off()
                    green.on()
                    disabled=False
                else:
                    print()
                    print('incorrect code')
                    #check_star()
             
        elif not disabled:
            #while True:
                if check_distance(0.09):
                    if check_star():
                        print ('Enter code to turn off the alarm')
                        password = passwords(password)
                        if check_code(password, correct):
                            disabled = False
                            buzzer.off()
                            green.off()
                            red.off()
                            blue.on()
                            print('correct code')
                           
                        else:
                            print('incorrect code')
                    if check_star():
                        print ('Enter code to disarm the system')
                        password = passwords(password)
                        if check_code(password, correct):
                            disabled = True
                            buzzer.off()
                            blue.off()
                            green.on()
                            print('disabled')
                       
           
 
main()

