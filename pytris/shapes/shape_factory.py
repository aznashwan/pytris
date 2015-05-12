import random
from pytris.shapes import *


class ShapeFactory(object):
    __shapes = [JShape, LineShape, LShape, SquareShape, TShape, ZShape, SShape]

    @staticmethod
    def get_random_shape():
        return random.choice(ShapeFactory.__shapes)()
