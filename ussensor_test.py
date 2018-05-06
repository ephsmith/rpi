# -*- coding: utf-8 -*-
# Author: Forrest Smith
from ussensor import ussensor
import RPi.GPIO as io
from time import sleep


test_cases = {'poll': {'echo': 17, 'trigger': 4, 'poll': True},
              'interrupt': {'echo': 17, 'trigger': 4, 'poll': False}}
# test_cases = {'poll': {'echo': 17, 'trigger': 4, 'poll': True}}


for case, opts in test_cases.items():
    s = ussensor(**opts)
    sleep(1)
    print('\nPrinting {} Range Measurements:\n'.format(case))
    for k in range(4):
        print(s.distance())
        sleep(1)
    print('\nDone!!!\n')
    del s

io.cleanup()
