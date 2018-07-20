# -*- coding: utf-8 -*-
# Author: Forrest Smith
from guizero import App, Text, PushButton, Slider
from guizero import TextBox, Combo, MenuBar
from rpi.arm import Arm
import serial
from sys import platform
from tkinter import filedialog
import json


home = {k: 50 for k in ('base', 'shoulder',
                        'elbow', 'wrist',
                        'gripper')}

poses = {'home': home}

app = App(title='Arm Poser', layout='grid')

# The SC shows up as different devices on different OSes
if platform == 'darwin':
    com = serial.Serial('/dev/tty.usbserial-AK05CSCD', 9600)
else:
    com = serial.Serial('/dev/ttyUSB0', 9600)

arm = Arm(com=com)


def get_pose():
    return {k: v for k, v in zip(('base', 'shoulder',
                                  'elbow', 'wrist', 'gripper'),
                                 (base.value, shoulder.value, elbow.value,
                                  wrist.value, gripper.value))}


def save_pose():
    # print('Pose to save: {}\n{}'.format(pose_name.value, get_pose()))
    poses[pose_name.value] = get_pose()
    pose_combo.append(pose_name.value)
    pose_name.clear()


def update_pose():
    """Update the current pose with the values of the sliders"""
    poses[pose_name.value] = get_pose()


def update_sliders(key):
    d = poses[key]
    base.value = d['base']
    shoulder.value = d['shoulder']
    elbow.value = d['elbow']
    wrist.value = d['wrist']
    gripper.value = d['gripper']


def delete_pose():
    key = pose_combo.value
    pose_combo.remove(key)
    poses.pop(key, None)


def move():
    arm.move(**get_pose())


def save():
    filename = filedialog.asksaveasfilename(initialdir='~/',
                                            title='Save file',
                                            filetypes=(('JSON files',
                                                        '*.json')))
    with open(filename + '.json', 'w') as f:
        json.dump(poses, f)


def load():
    filename = filedialog.askopenfilename(initialdir='~/',
                                          title='Open file',
                                          filetypes=(('JSON files', '*.json')))
    with open(filename, 'r') as f:
        poses = json.load(f)

    pose_combo.clear()
    for k in poses.keys():
        pose_combo.append(k)


menubar = MenuBar(app,
                  toplevel=['File'],
                  options=[
                      [['Save Poses', save], ['Load Poses', load]],
                  ])

base = Slider(app, grid=[1, 0], start=1, end=100)
shoulder = Slider(app, grid=[1, 1], start=1, end=100)
elbow = Slider(app, grid=[1, 2], start=1, end=100)
wrist = Slider(app, grid=[1, 3], start=1, end=100)
gripper = Slider(app, grid=[1, 4], start=1, end=100)

for s in (base, shoulder, elbow, wrist, gripper):
    s.value = 50
    s.width = 350


base_text = Text(app, text='Base',
                 grid=[0, 0], align='left')
shoulder_text = Text(app, text='Shoulder',
                     grid=[0, 1], align='left')
elbow_text = Text(app, text='Elbow',
                  grid=[0, 2], align='left')
wrist_text = Text(app, text='Wrist',
                  grid=[0, 3], align='left')
gripper_text = Text(app, text='Gripper',
                    grid=[0, 4], align='left')

for t in (base_text, shoulder_text, elbow_text,
          wrist_text, gripper_text):
    t.width = 10

move_button = PushButton(app, text='Move', command=move,
                         grid=[1, 5], align='right')

pose_name = TextBox(app, grid=[1, 6], align='right')
pose_name.width = 16

save_button = PushButton(app, text='Save Pose', align='right',
                         grid=[1, 7], command=save_pose)

pose_combo = Combo(app, options=['home'], align='right',
                   grid=[1, 8], command=update_sliders)

pose_combo.width = 16

pose_delete_button = PushButton(app, text='Delete Pose', align='right',
                                grid=[1, 10], command=delete_pose)

pose_update_button = PushButton(app, text='Update Pose', align='right',
                                grid=[1, 9], command=update_pose)
app.display()
