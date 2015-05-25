

class Board(object):
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, matrix=None):
        if matrix is None:
            self._board = [[None for _ in range(Board.WIDTH)] for _ in range(Board.HEIGHT)]
        else:
            self._board = matrix

    def check_on_board(self, piece):
        for x, y in piece.coordinates:
            if x < 0 or x > self.WIDTH - 1 or y < 0 or y > self.HEIGHT - 1:
                return False
        return True

    def check_overlap(self, piece):
        for x, y in piece.coordinates:
            if self.check_on_board(piece) and self._board[y][x] is not None:
                return False
        return True

    def remove_full_rows(self):
        k = 0
        for index in self._get_full_rows():
            self._board.pop(index)
            self._board.insert(0, [None for _ in range(self.WIDTH)])
            k += 1

        return k

    def get_active_blocks(self):
        blocks = []
        for row_k, row in enumerate(self._board):
            for col_k, item in enumerate(row):
                if item is not None:
                    blocks.append((row_k, col_k, item))
        return blocks

    def _get_full_rows(self):
        rows = []

        for row_index, row in enumerate(self._board):
            if None not in row:
                rows.append(row_index)

        return rows

    def lock(self, piece):
        blocks = piece.coordinates
        for (x, y) in blocks:
            self._board[x][y] = piece.color

    @staticmethod
    def get_spawn():
        return (Board.WIDTH - 4) // 2, 0

    def __str__(self):
        string = ''

        for row in self._board:
            for item in row:
                string += str(item) + ' '
            string += '\n'

        return string

    def __repr__(self):
        return self.__str__()
