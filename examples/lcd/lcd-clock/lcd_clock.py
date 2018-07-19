# -*- coding: utf-8 -*-
# Author: Forrest Smith
# Title:  lcd.py

from rpi.lcd import lcd
import time
import serial

def delay(d):
    '''
	delay: poll the clock until d seconds have passed
    '''
    target = time.clock() + d
    while time.clock() < target:
        pass


# open the serial port
com = serial.Serial('/dev/ttyS0', 9600)

# instantiate an lcd object. Note
# pass the serial stream object to the
# lcd object.
disp = lcd(com=com)

# Test basic display functions
disp.set_brightness(1)
time.sleep(1)
disp.set_brightness(5)
disp.display_version()  # firmware ver is displayed
time.sleep(2)
disp.command(disp.CLEAR_SCREEN)
# Now, make a basic clock using the lcd as a
# display.
#
# NOTE: This loop will run indefinitely. Use CTRL-C
# to terminate the loop.
while True:

    # use strftime to format the time string
    # appropriately. See strftime documentation
    disp.text(time.strftime('%I:%M:%S %p'))
    disp.set_cursor(0)
    # call our custom delay
    delay(0.5)

    # clear the screen
    # disp.command(disp.CLEAR_SCREEN)
