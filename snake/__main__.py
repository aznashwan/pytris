from snake.matrix import Matrix
from snake.snake import Snake

board = Matrix()
game = Snake(board)
game.run()


# Testing area

# from snake.pixel import Pixel
#
# game = Snake(None)

# Test simple movement
# game.food = Pixel(7, 7, Snake.FOOD_COLOR)
# game.last_direction = (1, 0)
# print(game.last_direction)
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)


# Test simple food collision
# game.segments = [Pixel(1, 4, "blah"), Pixel(0, 4, "blah")]
# game.food = Pixel(2, 4, "food")
# game.last_direction = (1, 0)
# print(game.last_direction)
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)

# Test collision
# game.segments = [Pixel(1, 4, "blah"), Pixel(2, 4, "blah")]
# game.food = Pixel(3, 4, "food")
# game.last_direction = (1, 0)
# print(game.last_direction)
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)
# print(game.lost, game.running)


# Test wraparound
# game.segments = [Pixel(0, 4, "blah"), Pixel(1, 4, "blah")]
# print(game.segments, game.food)
# game.last_direction = (-1, 0)
# game.ripple()
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)
#
# print()
#
# game.segments = [Pixel(7, 0, "blah"), Pixel(6, 0, "blah")]
# print(game.segments, game.food)
# game.last_direction = (1, 0)
# game.ripple()
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)
#
# print()
#
# game.segments = [Pixel(0, 0, "blah"), Pixel(1, 0, "blah")]
# print(game.segments, game.food)
# game.last_direction = (0, -1)
# game.ripple()
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)
#
# print()
#
# game.segments = [Pixel(0, 7, "blah"), Pixel(1, 7, "blah")]
# print(game.segments, game.food)
# game.last_direction = (0, 1)
# game.ripple()
# print(game.segments, game.food)
# game.ripple()
# print(game.segments, game.food)


# Test direction change 180 case, and read_direction reset
# game.segments = [Pixel(0, 7, "blah"), Pixel(1, 7, "blah")]
# print(game.segments, game.food)
# game.last_direction = (0, 1)
# print(game.last_direction)
#
# game.read_direction = (1, 0)
# game._update_motion()
# print(game.last_direction)
# print(game.read_direction)