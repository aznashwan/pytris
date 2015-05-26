from pytris.matrix import Matrix
from pytris.snake import Snake


board = Matrix()

game = Snake(board)
game.run()