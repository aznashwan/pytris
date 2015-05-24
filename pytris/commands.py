import queue
from threading import Thread
import time
from pytris.keyboard import get_key


class Commands(object):
    def __init__(self, game):
        self._game = game
        self.commands = queue.Queue(0)

        Thread(target=self.control).start()
        Thread(target=self.process).start()

    def control(self):
        while 1:
            command = get_key()
            self.commands.put(command)

            if command == self._game.BTN_EXIT:
                break

    def process(self):
        while 1:
            try:
                command = self.commands.get(False)
            except queue.Empty as e:
                command = ""

            if command == "q":
                self._game.finish()
                break

            # TODO process command input and callback in game

            # wait anyway for a second, you can tweak that
            time.sleep(1./self._game.FPS)

