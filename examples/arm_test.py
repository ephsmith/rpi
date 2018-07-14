# -*- coding: utf-8 -*-
# Author: Forrest Smith
#
#

import serial
from rpi.arm import Arm
import time

# Open up the USB port for serial comm
com = serial.Serial('/dev/ttyUSB0', 9600)

# instantiate an Arm object
a = Arm(com=com)

# move the arm to the default position
a.move()
time.sleep(5)
# move them all to 10%
a.move(base=30,
       shoulder=30,
       elbow=30,
       wrist=30,
       gripper=30)

time.sleep(5)
# save that position for later use
p1 = a.dump_params()

# move the arm to the home position
a.home()
print("Test complete. Bye!")
