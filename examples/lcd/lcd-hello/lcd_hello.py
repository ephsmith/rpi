# -*- coding: utf-8 -*-
# Author: Forrest Smith
# Title:  lcd_hello.py

from rpi.lcd import lcd
import serial
from time import sleep

# open the serial port
com = serial.Serial('/dev/ttyS0', 9600)

# instantiate an lcd object. Note
# pass the serial stream object to the
# lcd object.
disp = lcd(com=com)

# Test basic display functions
disp.set_brightness(1)
sleep(1)
disp.set_brightness(5)
disp.display_version()  # firmware ver is displayed
sleep(2)
disp.command(disp.CLEAR_SCREEN)
sleep(1)


# NOTE: This loop will run indefinitely. Use CTRL-C
# to terminate the loop. In IDLE, you may need to
# restart the python shell.
while True:
    disp.clear()
    text = input()
    disp.text(text)
