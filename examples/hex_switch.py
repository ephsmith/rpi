# -*- coding: utf-8 -*-
# Author: Forrest Smith
import RPi.GPIO as gpio
import time

'''
HEX Switch Interface

Switch  |  BCM Pin
------------------
1       |    16
2       |    18
3       |    23
4       |    24
------------------

'''

# Configure the channels in software
bit_0 = 16
bit_1 = 18
bit_2 = 23
bit_3 = 24
inputs = (bit_3, bit_2, bit_1, bit_0)

# Use BCM pin numbers
gpio.setmode(gpio.BCM)

# SEt the internal pulldown resistors
for channel in inputs:
    gpio.setup(channel, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# Base output string

try:
# Loop forever and read the input states every 2 seconds.
    while True:
        s = ''
        num = 0
        for n,b in enumerate(inputs):
                if gpio.input(b):
                    s += '1'
                    num += 2 ** (3-n)
                else:
                    s += '0'
                    
        print('Decimal: {}, Hex: 0x{:1X} Binary: {}'.format(num, num, s))
        time.sleep(2)
except KeyboardInterrupt:
    print('Thanks for switching!  Bye!')

                
