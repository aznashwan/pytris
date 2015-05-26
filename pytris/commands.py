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
            "w": self._game.queue_up,
            "a": self._game.queue_left,
            "s": self._game.queue_down,
            "d": self._game.queue_right,
            " ": self._game.finish
        }

    def control(self):
        while 1 and self._game.running:
            command = get_key()
            self.commands.put(command)
            time.sleep(0.016)

            if command == " ":
                break

    def process(self):
        while not self.commands.empty():
            command = self.commands.get(False)

            if command in self._instructions:
                self._instructions[command]()

            time.sleep(0.016)