"""
    Copyright 2015 Nashwan Azhari, Krody Robert.
    Licensed under the GPLv2 license. See LICENSE file for details.
"""


class Pixel(object):
    """
        The basic class representing a pixel.
        Contains an X and Y coordinate alongside the color of the pixel.
    """

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color