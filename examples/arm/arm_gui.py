# -*- coding: utf-8 -*-
# Author: Forrest Smith
from guizero import App, Text, PushButton, Slider


app = App(title='Sliders', layout='grid')
base = Slider(app, grid=[1, 0], start=1, end=100)
shoulder = Slider(app, grid=[1, 1], start=1, end=100)
elbow = Slider(app, grid=[1, 2], start=1, end=100)
wrist = Slider(app, grid=[1, 3], start=1, end=100)
gripper = Slider(app, grid=[1, 4], start=1, end=100)

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
move_button = PushButton(app, text='Move',
                         grid=[1, 5])

app.display()
