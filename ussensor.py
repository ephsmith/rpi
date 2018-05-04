# -*- coding: utf-8 -*-
# Author: Forrest Smith
import RPi.GPIO as io
import time


class USSensor():
    '''Simple class for interfacing an HC-SR04'''

    def __init__(self, echo=None, trigger=None):
        self._echo = echo
        self._trigger = trigger
        self._pulse_begin = 0
        self.distance = None  # default value for unmeasured distance
        io.setmode(io.BCM)
        io.setup(self._echo, io.IN)
        io.setup(self._trigger, io.OUT)
        io.add_event_detect(self._echo,
                            io.BOTH,
                            callback=self._stamp_times)
        io.output(self._trigger, False)
        time.sleep(0.000005)
        io.output(self._trigger, True)
        time.sleep(0.00001)
        io.output(self._trigger, False)

    def _stamp_times(self, channel):
        if io.input(self._echo):
            self._pulse_begin = time.time()
        else:
            self.distance = (time.time() - self._pulse_begin) * 34300 / 2
            io.output(self._trigger, True)
            time.sleep(0.00001)
            io.output(self._trigger, False)


# Test Driver
sensor = USSensor(echo=17, trigger=4)
try:
    while True:
        print(sensor.distance)
        time.sleep(1)
except KeyboardInterrupt:
    print('\n' + '#' * 15 + '\tExiting\t' + '#' * 15)
    io.cleanup()
    print('GPIO Cleanup Complete!!')
