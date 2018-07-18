# -*- coding: utf-8 -*-
# Author: Forrest Smith
import serial
from time import sleep
from rpi.arm import Arm

# Open the serial port
com = serial.Serial('/dev/ttyUSB0',9600)

"""
Create an instance of the Arm class and 
pass it the serial object for communication.
"""
a = Arm(com=com)


"""
Arm objects have 5 "joints" that can be manipulated:

+-----------+-----------+
|  Joint    |  range    |
+-----------+-----------+
|  base     | (1 to 100)|
|  shoulder | (1 to 100)|
|  elbow    | (1 to 100)|
|  wrist    | (1 to 100)|
|  gripper  | (1 to 100)|
+-----------+-----------+
"""

# Arm positions default to the midpoint of 50
a.move() # moves all servos using current values

# Change the value of a joint
a.shoulder = 40 # now shoulder value is 40

# Since we changed the value of the shoulder attribute,
# calling the `move` method again will move
# the shoulder servo.
# Check with the user first :)
response = input('\nMove shoulder to rotation 40? (y or n): ')
if 'y' in response.lower():
    a.move()

# We can also pass one or more joint parameters directly
# to the move method.
response = input('\nMoving most joints to rotation 60. ok? (y or n): ')
if 'y' in response.lower():
    a.move(base=60, shoulder=60, elbow=60, wrist=60)

# How do we get back to the default position?
# There are two approaches:
# 1. move all joints to rotation 50
# 2. (simpler) use the default_params method
a.default_params()

response = input('\nReturn all joints to default rotation? (y or n): ')
if 'y' in response:
    a.move()

# What about saving a specific pose?
# Use the dump_params method.

response = input('\nMove wrist=40, shoulder=60? (y or n): ')
if 'y' in response:
    a.wrist = 40
    a.move(shoulder=60) # shoulder is 60 and wrist is 40, others are 50
    response = input('\nSave position? (y or n): ')
    if 'y' in response:
        pose_1 = a.dump_params()
        print('\nParamters {} saved to variable pose_1'.format(pose_1))


response = input("\nI'm about to do a little dance. Ready? (y or n) ")
if 'y' in response:
    try:
        # Hopefully the user said yes to everything :)
        # Just in case, lets set save a pose to pose_1 and move
        # back and forth between home and that pose.
        a.wrist = 40
        a.shoulder = 60
        a.elbow = 40
        pose_1 = a.dump_params()
        
        while True:
            a.default_params()
            a.move()
            sleep(.5)
            a.move(**pose_1)
            sleep(.5)
    except KeyboardInterrupt:
        print('Hopefully you enjoyed my little dance!\nBye!')
else:
    print('That gives me a sad :(.  Thanks anyway!')

        
