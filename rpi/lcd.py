# -*- coding: utf-8 -*-
# Author: Forrest Smith
# Title:  lcd.py


class lcd(object):
    PREFIX = 0xFE
    DISPLAY_ON = 0x41
    DISPLAY_OFF = 0x42
    SET_CURSOR = 0x45
    CURSOR_HOME = 0x46
    UNDERLINE_CURSOR_ON = 0x47
    UNDERLINE_CURSOR_OFF = 0x48
    CURSOR_LEFT = 0x49
    CURSOR_RIGHT = 0x4A
    BLINKING_CURSOR_ON = 0x4B
    BLINKING_CURSOR_OFF = 0x4C
    BACKSPACE = 0x4E
    CLEAR_SCREEN = 0x51
    SET_CONTRAST = 0x52
    SET_BRIGHTNESS = 0x53
    DISPLAY_LEFT = 0x55
    DISPLAY_RIGHT = 0x56
    DISPLAY_VERSION = 0x70

    def __init__(self, com=None):
        self.com = com

    def command(self, command, value=None):
        '''
        command sends a command to the display.

        HINT: Use the built-in class constants for commands
        lcd.command(lcd.DISPLAY_VERSION)
        '''
        if command in (self.SET_CURSOR,
                       self.SET_CONTRAST,
                       self.SET_BRIGHTNESS):
            if value is not None:
                self.com.write(bytes([self.PREFIX,
                                      command,
                                      value]))
            else:
                raise ValueError('Command requires an argument')
        else:
            self.com.write(bytes([self.PREFIX, command]))

    def set_cursor(self, position):
        '''
        set_cursor moves the cursor the the position of value which
        should be in the range [0,103] decimal or [0x00, 0x67] hex.

        Note: only values from [0,15] and [0,79] decimal or [0x00,0x0F]
        and [0x40,0x4F] are visible.
        '''
        if position >= 0x00 and position <= 0x67:
            self.command(self.SET_CURSOR, value=position)
        else:
            raise ValueError('position must be in the range [0,103] decimal')

    def display_on(self):
        self.command(self.DISPLAY_ON)

    def display_off(self):
        self.command(self.DISPLAY_OFF)

    def display_version(self):
        self.command(self.DISPLAY_VERSION)

    def set_contrast(self, contrast):
        '''
        set_contrast: sets the contrast of the display to the value
        of contrast.

        NOTE: contrast should be in the range [1,50] decimal
        '''
        if contrast > 1 and contrast < 51:
            self.command(self.SET_CONTRAST, value=contrast)
        else:
            raise ValueError('Contrast must be in the range [1,50] decimal')

    def set_brightness(self, brightness):
        '''
        set_brightness: sets the brightness of the display to the value of
        brightness.

        NOTE: brightness should be in the range [1,8] decimal
        '''
        if brightness > 0 and brightness < 9:
            self.command(self.SET_BRIGHTNESS, value=brightness)
        else:
            raise ValueError('brightness should be in the range [1,8] decimal')

    def display_right(self):
        '''
        display_right: shifts the display to the right 1 space
        '''
        self.command(self.DISPLAY_RIGHT)

    def display_left(self):
        '''
        display_left: shifts the display to the left 1 space
        '''
        self.command(self.DISPLAY_LEFT)

    def text(self, msg):
        '''
        text: converts msg to an ASCII byte string and sends it to
        the lcd over serial.
        '''
        self.com.write(bytes(msg, 'ascii'))
