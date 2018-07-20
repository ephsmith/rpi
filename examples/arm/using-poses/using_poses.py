# -*- coding: utf-8 -*-
# Author: Forrest Smith
# Title: loaded_poses.py
#
# This file demonstrates the import and use of poses
# saved using the arm_gui.py script.
import serial
from rpi.arm import Arm
import time
import json

# Open up the USB port for serial comm
com = serial.Serial('/dev/ttyUSB0', 9600)

# instantiate an Arm object
a = Arm(com=com)

# load the poses from the JSON file
# this particular pose file contains 3 poses:
# home, min, and max
with open('pose-file.json', 'r') as f:
    poses = json.load(f)

# we can save the individual poses to new variables. Access
# each pose by name (remember, poses is a dictionary).
home = poses['home']  # dictionary containing home params
min = poses['min']
max = poses['max']

# We have to pass the poses to the move() method in a special
# way
a.move(**home)
time.sleep(5)
a.move(**min)
time.sleep(5)
a.move(**max)

# If you want to loop over several poses in order, start with
# a tuple of pose names.
loop_poses = ('min', 'max')
for p in loop_poses:
    this_pose = poses[p]
    a.move(**this_pose)
    time.sleep(2)
