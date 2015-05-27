import copy
from time import time
from snake.collision import Collision
from snake.color import Color
from snake.commands import Commands
from snake.lcd import LCD
from snake.pixel import Pixel
from random import randint


class Snake(object):
    WIDTH = 8
    HEIGHT = 8

    TICK_PER_SECOND = 60
    SKIP_TICKS = 1000 / TICK_PER_SECOND
    MAX_FRAME_SKIP = 5

    SNAKE_HEAD_COLOR = Color.green
    SNAKE_BODY_COLOR = Color.purple
    FOOD_COLOR = Color.white

    DIRECTIONS = {
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0),
        "up": (0, 1)
    }

    def __init__(self, board):
        self.food = None
        self.score = 0
        self.running = True
        self.lost = False

        self.segments = [Pixel(1, 4, self.SNAKE_HEAD_COLOR), Pixel(0, 4, self.SNAKE_BODY_COLOR)]
        self.spawn_food()

        self.last_direction = self.DIRECTIONS["right"]
        self.read_direction = None

        self.board = board
        self.commands = Commands(self)
        self.lcd = LCD()

        self.board.clear()
        self.lcd.clear()

    def run(self):
        next_update = time()
        while self.running:
            loops = 0
            while time() > next_update and loops < self.MAX_FRAME_SKIP:
                self.commands.process()
                self.ripple()

                next_update += self.SKIP_TICKS
                loops += 1

            self.draw()

        self.draw_end()

    def draw(self):
        for segment in self.segments:
            self.board.write_pixel(segment)

        self.board.clear()
        self.board.write_pixel(self.food)
        self.board.write()

        self.lcd.clear()
        self.lcd.writeline("Score {:s}".format(self.score))

    def draw_end(self):
        if not self.lost:
            return

        red = Color.red
        # Giant red X
        lose_pixels = [(0, 0, red), (1, 1, red), (2, 2, red), (3, 3, red),
                       (4, 4, red), (5, 5, red), (6, 6, red), (7, 7, red),
                       (7, 0, red), (6, 1, red), (5, 2, red), (4, 3, red),
                       (3, 4, red), (2, 5, red), (1, 6, red), (0, 7, red)]
        self.board.clear()
        for pixel in lose_pixels:
            self.board.write_pixel(pixel)
        self.board.write()

    def spawn_food(self):
        while True:
            x = randint(0, self.WIDTH - 1)
            y = randint(0, self.HEIGHT - 1)

            collisions = 0
            for segment in self.segments:
                if segment.x == x and segment.y == y:
                    collisions += 1
                    break

            if 0 == collisions:
                self.food = Pixel(x, y, self.FOOD_COLOR)
                break

    def _update_motion(self):
        head = self.segments[0]
        body = self.segments[1]

        # update the move direction making sure that the snake can't 180
        if self.read_direction is not None:
            delta = self.read_direction
            new_head = copy.copy(head)
            new_head.x = head.x + delta[0]
            new_head.y = head.y + delta[1]

            if not (new_head.x == body.x and new_head.y == body.y):
                self.last_direction = delta

            self.read_direction = None

    def _check_collisions(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if segment.x == head.x and segment.y == head.y:
                return Collision.SEGMENT

        if head.x == self.food.x and head.y == self.food.y:
            return Collision.FOOD
        return Collision.NONE

    def ripple(self):
        self._update_motion()

        head = self.segments[0]
        new_head = copy.deepcopy(head)
        new_head.x = (head.x + self.last_direction[0]) % self.WIDTH
        new_head.y = (head.y + self.last_direction[1]) % self.HEIGHT
        head.color = self.SNAKE_BODY_COLOR

        # Add a new segment as the new head
        self.segments.insert(0, new_head)

        collision_type = self._check_collisions()
        if collision_type is Collision.FOOD:
            self.spawn_food()
            self.score += 1
        elif collision_type is Collision.SEGMENT:
            self.segments.pop(0)
            self.segments[0].color = self.SNAKE_HEAD_COLOR
            self.running = False
            self.lost = True
        else:
            self.segments.pop()

        if len(self.segments) == self.WIDTH * self.HEIGHT:
            self.running = False

    def finish(self):
        self.running = False
        self.lost = True
