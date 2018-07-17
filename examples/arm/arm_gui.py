# -*- coding: utf-8 -*-
# Author: Forrest Smith
from guizero import App, Text, PushButton, Slider
from guizero import TextBox, Combo

home = {k: 50 for k in ('base', 'shoulder',
                        'elbow', 'wrist',
                        'gripper')
        }

poses = {'home': home}

app = App(title='Sliders', layout='grid')


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


base = Slider(app, grid=[1, 0], start=1, end=100)
shoulder = Slider(app, grid=[1, 1], start=1, end=100)
elbow = Slider(app, grid=[1, 2], start=1, end=100)
wrist = Slider(app, grid=[1, 3], start=1, end=100)
gripper = Slider(app, grid=[1, 4], start=1, end=100)

for s in (base, shoulder, elbow, wrist, gripper):
    s.value = 50


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

pose_name = TextBox(app, grid=[0, 6])

save_button = PushButton(app, text='Save Pose',
                         grid=[0, 7], command=save_pose)

pose_combo = Combo(app, options=['home'], grid=[2, 0], command=update_sliders)
pose_combo.width = 30

pose_delete_button = PushButton(app, text='Delete Pose',
                                grid=[2, 1], command=delete_pose)

app.display()
