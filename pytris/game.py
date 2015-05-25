from time import time
from pytris.board import Board
from pytris.commands import Commands
# from pytris.lcd import LCD
from pytris.pixel import Pixel
from pytris.tetramino import Tetramino


class Game(object):
    END_MESSAGE_1 = 'GAME OVER'
    END_MESSAGE_2 = 'SCORE %d'

    def __init__(self):
        self._score = 0
        self.running = True
        self._game_over = False

        self._rate = 1. / 60

        self._board = Board()
        self._spawn_new_piece()

        # self.lcd   = LCD()
        self.commands = Commands(self)

    def run(self):
        previous = time()
        lag = 0.

        while self.running:
            current = time()
            elapsed = current - previous
            previous = current
            lag += elapsed

            self.commands.process()

            while lag >= self._rate:
                self._update()
                lag -= self._rate

            self._display()

    def _update(self):
        self._increase_score(self._board.remove_full_rows())
        self.falling_move_down()

        # TODO update score message on lcd etc

    def _display(self):
        # TODO clear grid / set to black

        blocks = self._board.get_active_blocks()
        for (x, y) in self.falling_piece.coordinates:
            blocks.append(Pixel(x, y, self.falling_piece.color))

        pixels = []
        for (x, y, color) in blocks:
            pixels.append(Pixel(x, y, color))

        # Todo color grid
        # Todo flush to grid

    def falling_move_down(self):
        self.falling_piece.move_down()
        if not self._board.check_on_board(self.falling_piece):
            self.falling_piece.move_up()
        elif not self._board.check_overlap(self.falling_piece):
            self.falling_piece.move_up()
            self._board.lock(self.falling_piece)

    def falling_move_left(self):
        self.falling_piece.move_left()
        if not self._board.check_on_board(self.falling_piece):
            self.falling_piece.move_right()
        elif not self._board.check_overlap(self.falling_piece):
            self.falling_piece.move_right()
            self._board.lock(self.falling_piece)

    def falling_move_right(self):
        self.falling_piece.move_right()
        if not self._board.check_on_board(self.falling_piece):
            self.falling_piece.move_left()
        elif not self._board.check_overlap(self.falling_piece):
            self.falling_piece.move_left()
            self._board.lock(self.falling_piece)

    def falling_rotate(self):
        self.falling_piece.rotate(1)
        if not self._board.check_on_board(self.falling_piece):
            self.falling_piece.rotate(-1)
        elif not self._board.check_overlap(self.falling_piece):
            self.falling_piece.rotate(-1)
            self._board.lock(self.falling_piece)

    def _spawn_new_piece(self):
        self.falling_piece = Tetramino()
        self.falling_piece.warp(*self._board.get_spawn())

        if not self._board.check_overlap(self.falling_piece):
            self.running = False

    def finish(self):
        self.running = False

    def _increase_score(self, amount):
        self._score += amount * 10