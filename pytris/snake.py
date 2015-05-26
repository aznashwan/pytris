import copy
from pytris.collision import Collision
from pytris.color import Color
from pytris.commands import Commands
from pytris.lcd import LCD
from pytris.pixel import Pixel
from random import randint


class Snake(object):
    WIDTH  = 8
    HEIGHT = 8

    SNAKE_HEAD_COLOR = Color.green
    SNAKE_BODY_COLOR = Color.purple
    FOOD_COLOR       = Color.white

    DIRECTIONS = {
        "right": (1, 0),
        "down": (0, 1),
        "left": (-1, 0),
        "up": (0, 1)
    }

    def __init__(self, board):
        self.segments = [Pixel(3, 4, self.SNAKE_HEAD_COLOR), Pixel(4, 4, self.SNAKE_BODY_COLOR)]
        self.food     = self.spawn_food()
        self.last_direction = self.DIRECTIONS["right"]
        self.read_direction = None
        self.score = 0
        self.running = True
        self.lost = False

        self.board = board
        self.commands = Commands(self)
        # self.lcd = LCD()

    def run(self):
        while self.running:
            self.board.clear()
            self.ripple()
            self.draw()
            #self.lcd.clear()
            #self.lcd.writeline("Score %s" % self.score)

        self.board.clear()
        self.draw_end()

    def queue_up(self):
        self.read_direction = self.DIRECTIONS["up"]

    def queue_down(self):
        self.read_direction = self.DIRECTIONS["down"]

    def queue_left(self):
        self.read_direction = self.DIRECTIONS["left"]

    def queue_right(self):
        self.read_direction = self.DIRECTIONS["right"]

    def finish(self):
        self.running = False
        self.lost    = True

    def draw(self):
        for segment in self.segments:
            self.board.write_pixel(segment)

        self.board.write_pixel(self.food)
        self.board.write()

    def draw_end(self):
        if self.lost:
            pass # TODO add lose screen

    def spawn_food(self):
        while True:
            x = randint(0, self.WIDTH)
            y = randint(0, self.HEIGHT)

            collisions = 0
            for segment in self.segments:
                if segment.x == x and segment.y == y:
                    collisions += 1
                    break

            if 0 == collisions:
                return Pixel(x, y, self.FOOD_COLOR)

    def check_collisions(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if segment.x == head.x and segment.y == head.y:
                return Collision.SEGMENT

        if head.x == self.food.x and head.y == self.food.y:
            return Collision.FOOD
        return Collision.NONE

    def ripple(self):
        head = self.segments[0]
        body = self.segments[1]
        if self.read_direction is not None:
            delta = self.read_direction
            new_head = copy.copy(head)
            new_head.x = head.x + delta.x
            new_head.y = head.y + delta.y

            if not(new_head.x == body.x and new_head.y == body.y):
                self.last_direction = delta

            self.read_direction = None

        old_head = copy.copy(head)
        head.x = self.last_direction[0] % self.WIDTH
        head.y = self.last_direction[1] % self.HEIGHT

        collision_type = self.check_collisions()
        if collision_type is Collision.FOOD:
            old_head.color = self.SNAKE_BODY_COLOR
            self.segments.insert(1, old_head)
            self.spawn_food()
            self.score += 10
        elif collision_type is Collision.SEGMENT:
            head = old_head
            self.running = False
            self.lost = True
        else:
            # Head is moved only move body
            for segment in self.segments[1:]:
                seg_copy  = copy.copy(segment)
                segment.x = old_head.x
                segment.y = old_head.y

                old_head  = seg_copy

        if len(self.segments) == self.WIDTH * self.HEIGHT:
            self.running = False
