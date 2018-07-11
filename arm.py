def scale(num, min, max):
    '''
    For num between 0 and 100, returns number scaled to a range
    based on Garry's scaling.
    '''
    return min + int((num / 100.0) * (max))


class Arm(object):
    '''
    This class defines a command object to hold various
    parameters needed to build / send a serial command
    to the Lynxmotion controller.

    The command is sent using the `com' attribute. This should
    be a valid pyserial object.

    All parameters are optional but must be between 1 and 100.
    Default value is 50.
    '''
    def __init__(self, speed=50,
                 base=50, shoulder=50,
                 elbow=50, wrist=50, gripper=50, com=None):
        self.speed = speed
        self.base = base
        self.shoulder = shoulder
        self.elbow = shoulder
        self.wrist = wrist
        self.gripper = gripper
        self.com = com
        self.scale_params()

    def __str__(self):
        '''
        return a string representation of an Arm instance.
        Allows the use of print(my_arm)
        '''
        return vars(self).__str__()

    def __setattr__(self, attr, value):

        # Just assign the value for scaled attributes.
        if attr.startswith('_'):
            super().__setattr__(attr, value)
            return

        if attr == 'com':
            super().__setattr__(attr, value)
            return

        scaled_attr = '_' + attr
        if attr == 'speed':
            scaled_value = scale(value, 100, 900)
        else:
            scaled_value = scale(value, 500, 2000)
        super().__setattr__(attr, value)
        super().__setattr__(scaled_attr, scaled_value)

    def set_params(self, **kwargs):
        '''
        Update params based on key,value pairs in kwargs.
        Example:
        >>>my_arm = Arm()
        >>>my_arm.set_params(speed=100,base=50)

        or with a dictionary of key,value pairs
        >>>d = {'speed':100, 'base':50}
        >>>my_arm.set_params(**d)
        '''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def default_params(self):
        '''
        Returns all position parameters to the default of 50
        '''
        params = {'base': 50,
                  'shoulder': 50,
                  'elbow': 50,
                  'wrist': 50,
                  'gripper': 50,
                  'speed': 50}

        self.set_params(**params)

    def scale_params(self):

        self._speed = scale(self.speed, 100, 900)

        for attr in ('_base', '_shoulder', '_elbow', '_wrist', '_gripper'):
            setattr(self, attr,
                    scale(getattr(self, attr[1:]), 500, 2000))

    def dump_params(self):
        '''
        Returns a dictionary of position/speed params.

        This is especially useful when saving teach points.
        '''
        params = ('base', 'shoulder', 'elbow', 'wrist', 'gripper')
        return {p: getattr(self, p) for p in params}

    def to_command(self):
        '''Returns a command string for the current parameters'''
        param_list = [self._base, self._shoulder,
                      self._elbow, self._wrist,
                      self._gripper]

        s = ' '.join(['#{} P{} S{}'.format(k, param, self._speed)
                      for k, param in enumerate(param_list)])
        s = s + chr(13)

        return s.encode()

    def move(self):
        '''Sends the proper commands to the SCC32 using com'''
        self.com.write(self.to_command())
