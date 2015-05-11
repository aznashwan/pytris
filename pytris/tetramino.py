import random
from pytris.shapes import *


class Tetramino(object):
    __shapes = [JShape, LineShape, LShape, SquareShape, TShape, ZShape, SShape]

    def __init__(self, shape=None):
        if not shape:
            self.shape = self.get_random()
        else:
            self.shape = shape

    @staticmethod
    def get_random():
        return random.choice(Tetramino.__shapes)

