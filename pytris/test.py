# from pytris.board import Board
# from pytris.tetramino import Tetramino
#
# from pytris.shapes.square_shape import SquareShape
#
# matrix = [[None, None, None, None, None, None, None, None],
#           [None, None, None,    1,    1, None, None, None],
#           [None, None, None,    1,    1, None, None, None],
#           [None, None, None, None, None, None, None, None],
#           [None, None, None, None, None, None, None, None],
#           [None, None, None, None, None, None, None, None],
#           [None, None, None, None, None, None, None, None],
#           [   1,    1,    1,     1,   1,    1,    1,    1]]
#
# board = Board(matrix)
# piece = Tetramino(SquareShape())
#
# print(piece)
# print(piece.coordinates)
# # print(board.get_spawn())
# # print(board.check_collision(piece))
# # print(board)
# # print(board.remove_full_rows())
# # print(board)
#
#
# def check_collisions(p=Tetramino(SquareShape())):
#     p.warp(-2, 1)
#     print(board.check_on_board(p))
#     p.warp(0, -2)
#     print(board.check_on_board(p))
#     p.warp(0, 6)
#     print(board.check_on_board(p))
#     p.warp(6, 0)
#     print(board.check_on_board(p))
#     p.warp(3, 3)
#     print(board.check_on_board(p))
#
# # check_collisions()

from pytris.game import Game
game = Game()

while True:
    game.process_input()