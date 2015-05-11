from pytris.color import Color
from pytris.shapes.shape import Shape

__author__ = 'krotz'


class TShape(Shape):
    def __init__(self):
        super().__init__()
        self.states = [[[0, 0, 0, 0],
                        [0, 1, 1, 1],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]],

                       [[0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]],

                       [[0, 0, 1, 0],
                        [0, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]],

                       [[0, 0, 1, 0],
                        [0, 0, 1, 1],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]]]
        self.color = Color.white