from piece import *
import re


class ChessBoard(object):

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

    @staticmethod
    def _coord_to_index(coord: str):
        """convert string of coordinates into list of indexes"""
        if not re.match(r'^[a-h][1-8]$', coord.lower()):
            raise NameError('invalid coordinate %s' % coord)
        col = ord(coord[0].lower()) - 97  # convert ascii into int (97 ascii for 'a')
        row = int(coord[1], 10) - 1  # convert second char into int base10
        return [row, col]

    def move(self, start, to):
        from_row, from_col = ChessBoard._coord_to_index(start)
        to_row, to_col = ChessBoard._coord_to_index(to)
        print('%s => %d:%d' % (start, from_row, from_col))
        print('%s => %d:%d' % (to, to_row, to_col))
        if self.board[from_row][from_col]:
            print('found: %s' % self.board[from_row][from_col])
        else:
            print('empty')
        input('press ENTER')
        self.moves += 1

    def init(self):
        self._init_board()
