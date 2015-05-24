from pytris.board import Board
from pytris.keyboard import get_key
from pytris.commands import Commands
# from pytris.lcd import LCD


class Game(object):
    FPS = 60
    END_MESSAGE_1 = 'GAME OVER'
    END_MESSAGE_2 = 'SCORE %d'

    def __init__(self):
        self._score = 0
        # self._board = Board()
        # self.lcd   = LCD()
        self._running = True
        self._game_over = False
        self.commands = Commands(self)

    def finish(self):
        print('FINISHING')

    def _increase_score(self, amount):
        self._score += amount * 10

    def process_input(self):
        print(get_key())