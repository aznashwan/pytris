import queue
from threading import Thread
import time

from pytris.keyboard import get_key


class Commands(object):
    def __init__(self, game):
        self._game = game
        self.commands = queue.Queue(0)

        Thread(target=self.control).start()

        self._instructions = {
            "q": self._game.finish,
            "a": self._game.falling_move_left,
            "d": self._game.falling_move_right,
            " ": self._game.falling_rotate
        }

    def control(self):
        while 1 and self._game.running:
            command = get_key()
            self.commands.put(command)
            time.sleep(0.016)

            if command == "q":
                break

    def process(self):
        while not self.commands.empty():
            command = self.commands.get(False)

            if command in self._instructions:
                self._instructions[command]()

            time.sleep(0.016)