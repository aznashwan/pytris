'''
    Copyright 2015 Nashwan Azhari, Krody Robert.
    Licensed under the GPLv2 license. See LICENSE file for details.
'''
from enum import Enum

class Color(Enum):
    '''
        Basic enum of the 7 colors supported by the RGB matrix.
    '''
    white = 0b000
    blue = 0b001
    green = 0b010
    turquoise = 0b011
    red = 0b100
    purple = 0b101
    brown = 0b110
    black = 0b111

    def __init__(self, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)

