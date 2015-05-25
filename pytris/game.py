from time import time
from pytris.board import Board
from pytris.keyboard import get_key
# from pytris.commands import Commands
# from pytris.lcd import LCD
from pytris.shapes.shape_factory import ShapeFactory


class Game(object):
    END_MESSAGE_1 = 'GAME OVER'
    END_MESSAGE_2 = 'SCORE %d'

    def __init__(self):
        self._score = 0
        self._running = True
        self._game_over = False

        self._rate = 1. / 60

        self._board = Board()
        self._spawn_new_piece()

        print(self.falling_piece)
        # self.lcd   = LCD()
        # self.commands = Commands(self)

    def run(self):
        previous = time()
        lag = 0

        while True:
            current = time()
            elapsed = current - previous
            previous = current
            lag += elapsed

            # Process input here..

            while lag >= self._rate:
                self._update()
                lag -= self._rate

            self._display()



    def _update(self):
        pass

    def _display(self):
        pass





    def _spawn_new_piece(self):
        self.falling_piece = ShapeFactory.get_random_shape()
        self.falling_piece.warp(self._board.get_spawn())

    def finish(self):
        print('FINISHING')

    def _increase_score(self, amount):
        self._score += amount * 10

    def process_input(self):
        print(get_key())