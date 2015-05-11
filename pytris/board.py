class Board(object):
    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.board = [[None for _ in range(Board.HEIGHT)] for _ in range(Board.WIDTH)]
