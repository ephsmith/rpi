# -*- coding: utf-8 -*-
# Author: Forrest Smith
#
# Credits: Inspired by a python script authored by Garry Spencer


def scale(num, min, max):
    """
    For num between 0 and 100, returns number scaled to a range
    based on Garry"s scaling.
    """
    return min + int((num / 100.0) * (max))


class Arm(object):
    """
    This class defines a command object to hold various
    parameters needed to build / send a serial command
    to the Lynxmotion controller.

    The command is sent using the `com' attribute. This should
    be a valid pyserial object.

    All parameters are optional but must be between 1 and 100.
    Default value is 50.

    A note on servo channels:
    -------------------------
    The channels here are numbered from 0 to 4 with 0 being the
    base and 4 the gripper. Here is the full list of the channel
    assignments:

    CH | Servo
    ------------
    0  | base
    1  | shoulder
    2  | elbow
    3  | wrist
    4  | gripper
    _____________
    """

    def __init__(self, speed=50,
                 base=50, shoulder=50,
                 elbow=50, wrist=50,
                 gripper=50, com=None,
                 time=0):
        self.speed = speed
        self.base = base
        self.shoulder = shoulder
        self.elbow = shoulder
        self.wrist = wrist
        self.gripper = gripper
        self.com = com
        self.time = time
        self.scale_params()

    def __str__(self):
        """
        return a string representation of an Arm instance.
        Allows the use of print(my_arm)
        """
        return vars(self).__str__()

    def __setattr__(self, attr, value):

        # Just assign the value for scaled attributes.
        if attr.startswith('_'):
            super().__setattr__(attr, value)
            return

        if attr == 'com':
            super().__setattr__(attr, value)
            return

        if attr == 'time':
            if value >= 0 and value <= 65535:
                super().__setattr__(attr, int(value))
            else:
                raise ValueError(
                    '{}.time must be between 0 and 65535'.format(
                        self.__class__.__name__))
        scaled_attr = '_' + attr
        if attr == 'speed':
            scaled_value = scale(value, 100, 900)
        else:
            scaled_value = scale(value, 500, 2000)
        super().__setattr__(attr, value)
        super().__setattr__(scaled_attr, scaled_value)

    def set_params(self, **kwargs):
        """
        Update params based on key,value pairs in kwargs.
        Example:
        >>>my_arm = Arm()
        >>>my_arm.set_params(speed=100,base=50)

        or with a dictionary of key,value pairs
        >>>d = {'speed':100, 'base':50}
        >>>my_arm.set_params(**d)
        """

        # Assert that keys are valid class attributes
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise AttributeError(
                    '{}.{} is invalid parameter.'.format(
                        self.__class__.__name__, key))

        for key, value in kwargs.items():
            setattr(self, key, value)

    def default_params(self):
        """
        Returns all position parameters to the default of 50
        """
        params = {'base': 50,
                  'shoulder': 50,
                  'elbow': 50,
                  'wrist': 50,
                  'gripper': 50,
                  'speed': 50,
                  'time': 0}

        self.set_params(**params)

    def scale_params(self):

        self._speed = scale(self.speed, 100, 900)

        for attr in ('_base', '_shoulder', '_elbow', '_wrist', '_gripper'):
            setattr(self, attr,
                    scale(getattr(self, attr[1:]), 500, 2000))

    def dump_params(self):
        """
        Returns a dictionary of position/speed params.

        This is especially useful when saving teach points.
        """
        params = ('base', 'shoulder', 'elbow', 'wrist', 'gripper')
        return {p: getattr(self, p) for p in params}

    def to_command(self):
        """Returns a command string for the current parameters"""
        t = ''
        if self.time > 0:
            t = '{}'.format(self.time)

        param_list = [self._base, self._shoulder,
                      self._elbow, self._wrist,
                      self._gripper]

        s = ' '.join(['#{} P{} S{}'.format(k, param, self._speed)
                      for k, param in enumerate(param_list)])

        # Note. The T parameter affects all servos, so append it.
        s = s + t + chr(13)

        return s.encode()

    def home(self):
        """
        Returns all servos to the midpoint (home) position.
        """
        self.default_params()
        self.move()

    def move(self, **kwargs):
        """Sends the proper commands to the SCC32 using com"""
        if kwargs:
            self.set_params(**kwargs)
        self.com.write(self.to_command())
