# -*- coding: utf-8 -*-
# Author: Forrest Smith
import os
machine = os.uname().machine

from . import arm
from . import lcd

if machine == 'armv7l':
    '''This is a raspberrypi'''
    from . import ussensor
