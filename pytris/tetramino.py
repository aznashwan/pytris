from pytris.shapes.shape_factory import ShapeFactory


class Tetramino(object):

    def __init__(self, shape=None):
        if not shape:
            self._shape = ShapeFactory.get_random_shape()
        else:
            self._shape = shape

        self._x = 2
        self._y = 0
        self._occupied_coordinates()

    def warp(self, x, y):
        self._x = x
        self._y = y
        self._occupied_coordinates()

    def move_left(self):
        self._x -= 1
        self._occupied_coordinates()

    def move_right(self):
        self._x += 1
        self._occupied_coordinates()

    def move_down(self):
        self._y += 1
        self._occupied_coordinates()

    def move_up(self):
        self._y -= 1
        self._occupied_coordinates()

    def rotate(self, step=1):
        if step == 1:
            self._shape.rotate_cw()
        else:
            self._shape.rotate_ccw()
        self._occupied_coordinates()

    # TODO on rotate shift on the board :D
    # TODO game logic and keyboard interrupts

    def _occupied_coordinates(self):
        state = self._shape.current_state()
        occupied_coordinates = []

        for row_k, row in enumerate(state):
            for col_k, item in enumerate(row):
                if item == 1:
                    occupied_coordinates.append((self._x + col_k, self._y + row_k))

        self.coordinates = occupied_coordinates

    def __str__(self):
        return str(self._x) + ':' + str(self._y) + '\n' + str(self._shape)

    def __repr__(self):
        return repr(self._shape)