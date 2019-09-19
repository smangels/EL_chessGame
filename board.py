
from piece import *


class Board(object):

    def __init__(self):
        self.board = None
        self._init_board()

    def _init_board(self):
        if not self.board:
            _board = [[Rock('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rock('w')],
                      [Pawn('w') for x in range(8)], [None for x in range(8)], [None for x in range(8)],
                      [None for x in range(8)], [None for x in range(8)], [Pawn('b') for x in range(8)],
                      [Rock('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rock('b')]]
            self.board = _board.copy()

    def __str__(self):
        _str = "this is a board\n"
        _row = len(self.board)
        _str += "   A  B  C  D  E  F  G  H \n"
        for row in self.board:
            _str += "%d" % _row
            _row -= 1
            for tile in row:
                if tile:
                    _str += " %-2s" % tile
                else:
                    _str += "  x"

            _str += '\n'
        return _str

    def _init_from_file(self):
        pass


