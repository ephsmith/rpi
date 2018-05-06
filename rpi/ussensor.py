# -*- coding: utf-8 -*-
# Author: Forrest Smith
import RPi.GPIO as io
import time


class ussensor():
    '''Simple class for interfacing an HC-SR04

    Example:
    -------

    s = ussensor(echo=17, trigger=4)
    distance = s.distance

    Params:
    -------
    echo:    the BCM pin number of the RPi attached to echo
    trigger: the BCM pin number of the RPi attached to trigger
    poll:    Set poll=True to poll measurements instead of the
             default interrupt-based measurements

    Public Methods:
    ---------------
    ussensor.distance():
         returns the distance measurement. If poll=True, this is
         a 4 measurement average.  The default measurement method is
         interrupt-based and returns the current distance measurement.

    See the following for information on HC-SR04 hardware interfacing:

    https://projects.raspberrypi.org/en/projects/ultrasonic-theremin/4

    In short, use a voltage-divider to reduce the HC-SR04 ECHO output
    to acceptable levels for the RPi.
    '''

    def __init__(self, echo=None, trigger=None, poll=False):
        self._echo = echo
        self._trigger = trigger
        self._poll = poll
        self._pulse_begin = 0
        self._distance = 0
        io.setmode(io.BCM)
        io.setup(self._echo, io.IN)
        io.setup(self._trigger, io.OUT)
        if not self._poll:
            io.add_event_detect(self._echo,
                                io.BOTH,
                                callback=self._stamp_times)
            self._trigger_measurement()

    def _trigger_measurement(self):
        io.output(self._trigger, False)
        time.sleep(0.000005)
        io.output(self._trigger, True)
        time.sleep(0.00001)
        io.output(self._trigger, False)

    def _stamp_times(self, channel):
        if io.input(self._echo):
            self._pulse_begin = time.time()
        else:
            self._distance = (time.time() - self._pulse_begin) * 34300 / 2
            io.output(self._trigger, True)
            time.sleep(0.00001)
            io.output(self._trigger, False)

    def _measure(self):
        self._pulse_begin = time.time()
        pulse_end = time.time()
        self._trigger_measurement()

        while io.input(self._echo) == 0:
            self._pulse_begin = time.time()
        while io.input(self._echo) == 1:
            pulse_end = time.time()

        return (pulse_end - self._pulse_begin) * 34300 / 2

    def distance(self):
        if self._poll:
            m = 0
            # take four measurements and return the avg
            for k in range(4):
                m = (m + self._measure()) / 4
            return m
        else:
            return self._distance
