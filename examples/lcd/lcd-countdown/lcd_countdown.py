# -*- coding: utf-8 -*-
# Author: Forrest Smith
# Title:  lcd_countdown.py

from rpi.lcd import lcd
import serial
from time import sleep

# open the serial port
com = serial.Serial('/dev/ttyS0', 9600)

# instantiate an lcd object. Note
# pass the serial stream object to the
# lcd object.
disp = lcd(com=com)


# time till disaster in seconds
time_till_disaster = 15

while time_till_disaster > 0:
    disp.clear()
    sleep(0.2)
    disp.text('{}'.format(time_till_disaster))
    time_till_disaster -= 1  # subtract one second
    sleep(1)

# time_till_disaster is now 0 seconds
disp.text('{}'.format(time_till_disaster))
disp.text('Times UP!')
