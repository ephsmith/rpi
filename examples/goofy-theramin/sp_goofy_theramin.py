# -*- coding: utf-8 -*-
# Author: Forrest Smith
from ussensor import ussensor
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client
import RPi.GPIO as io

def clip_and_scale(p,
                   min_in=0,
                   max_in=100,
                   min_out=0,
                   max_out=50):
    '''
    clip p to input range {min_in, max_in} and
    scale the result to output range {min_out, max_out}

    example:

    opts = {'min_in': 0, 'max_in': 100,
            'min_out': 100, 'max_out': 200}

    >>> print(clip_and_scale(120, **opts))
    >>> 200
    '''
    p = max(min_in, min(max_in, p))
    m = max_out - min_out
    b = min_out
    normed = (p-min_in) / (max_in - min_in)
    return m*normed + b


sensor = ussensor(echo=17, trigger=4, poll=True)
sender = udp_client.SimpleUDPClient('localhost', 4559)
opts = {'min_in': 20, 'max_in': 200, 'min_out': 50, 'max_out': 80}

try:
    print('\nSending some notes!')
    while True:
        p = clip_and_scale(sensor.distance(), **opts)
        pitch = round(p)
        # sender.send_message('/play_this', pitch)
        sender.send_message('/play', pitch)
        sleep(0.2)
except KeyboardInterrupt:
    print('Bye!...')
    io.cleanup()
