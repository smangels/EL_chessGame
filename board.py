
from piece import *


class Board(object):

    def __init__(self):
        self.board = None
        self._init_board()
        self.moves = 0

    def _init_board(self):
        self.moves = 0
        _board = [[Rock('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rock('w')],
                  [Pawn('w') for x in range(8)], [None for x in range(8)], [None for x in range(8)],
                  [None for x in range(8)], [None for x in range(8)], [Pawn('b') for x in range(8)],
                  [Rock('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rock('b')]]
        self.board = _board.copy()

    def __str__(self):
        _row = len(self.board)
        _str = ""
        _str = "stats: %d moves\n" % self.moves
        _str += "     A   B   C   D   E   F   G   H \n\n"
        for row in self.board:
            _str += "%d  " % _row
            _row -= 1
            for tile in row:
                if tile:
                    _str += " %03s" % tile
                else:
                    _str += " %03s" % 'x'
            _str += '\n'
        return _str

    def _init_from_file(self):
        pass

    def move(self, start, to):
        print('move from %s to %s' % (start, to))
        self.moves += 1

    def init(self):
        self._init_board()


