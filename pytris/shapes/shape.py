from pytris.color import Color


class Shape(object):
    def __init__(self):
        self.states = [[]]
        self._current_state = 0
        self.color = Color.blue

    def rotate_cw(self):
        self._rotate(1)

    def rotate_ccw(self):
        self._rotate(-1)

    def _rotate(self, step=1):
        self._current_state = (self._current_state + step) % len(self.states)

    def current_state(self):
        return self.states[self._current_state]

    def __str__(self):
        string = ''

        for row in self.current_state():
            for item in row:
                string += str(item) + ' '
            string += '\n'

        return string

    def __repr__(self):
        return self.__str__()


