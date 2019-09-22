import re
from typing import List, Set
from piece import *


class CBNothingToMoveE(BaseException):
    def __init__(self, msg):
        self.msg = msg


class CBSameColorE(BaseException):
    def __init__(self, msg):
        self.msg = msg


class CBInvalidMove(BaseException):
    def __init__(self, msg):
        self.msg = msg


class CBInvalidColor(BaseException):
    def __init__(self, msg):
        self.msg = msg


class ChessBoard(object):

    def __init__(self):
        self.board = None
        self._init_board()
        self.moves = 0
        self.colornext = Color.WHITE

    def _init_board(self):
        self.moves = 0
        _board = [[Rock('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rock('b')],
                  [Pawn('b') for x in range(8)], [None for x in range(8)], [None for x in range(8)],
                  [None for x in range(8)], [None for x in range(8)], [Pawn('w') for x in range(8)],
                  [Rock('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rock('w')]]
        self.board = _board.copy()

    def __str__(self):
        _row = len(self.board)
        _str = ""
        _str = "next move: %s, stats: %d moves\n" % ('w' if self.colornext == Color.WHITE else 'b', self.moves)
        _str += "     A   B   C   D   E   F   G   H \n\n"
        for row in self.board:
            _str += "%d  " % _row
            _row -= 1
            for tile in row:
                if isinstance(tile, Piece):
                    _str += " %03s" % tile
                else:
                    _str += " %03s" % '.'
            _str += '\n'
        return _str

    def _init_from_file(self):
        pass

    @staticmethod
    def _coord_to_index(coord: str):
        """convert string of coordinates into row and column"""
        if not re.match(r'^[a-h][1-8]$', coord.lower()):
            raise NameError('invalid coordinate %s' % coord)
        col = ord(coord[0].lower()) - 97  # convert ascii into int (97 ascii for 'a')
        row = 8 - int(coord[1], 10)  # convert second char into int base10
        return [row, col]

    @staticmethod
    def _get_vector(orig: List[int], dest: List[int]) -> List[int]:
        vect_x = dest[0] - orig[0]
        vect_y = dest[1] - orig[1]
        return [vect_x, vect_y]

    def _register_valid_move(self):
        self.moves += 1
        if self.colornext == Color.WHITE:
            self.colornext = Color.BLACK
        else:
            self.colornext = Color.WHITE

    def move(self, start, to):
        """Move a piece from START to TO
            parameters:
                start: str
                    coordinates on a chess board
                to: str
                    coordinates on a chess board
        """
        from_row, from_col = ChessBoard._coord_to_index(start)
        to_row, to_col = ChessBoard._coord_to_index(to)
        vector = ChessBoard._get_vector([from_row, from_col], [to_row, to_col])

        orig = self.board[from_row][from_col]
        dest = self.board[to_row][to_col]
        _return = False

        if not orig:
            _return = False
            raise CBNothingToMoveE('nothing to move in %s' % start)

        if isinstance(orig, Piece):

            if orig.color != self.colornext:
                raise CBInvalidColor('black is next' if self.colornext == Color.BLACK else 'white is next')

            if not orig.validate_vector(vector):
                raise CBInvalidMove('invalid move for %s' % orig.get_long_name())

            if not dest:
                # move the piece directly to the new position
                self.board[to_row][to_col] = orig
                self.board[from_row][from_col] = None
                self._register_valid_move()
                _return = True
            else:  # remove something
                # check color
                if orig.color != dest.color:
                    self.board[to_row][to_col] = orig
                    self.board[from_row][from_col] = None
                    self._register_valid_move()
                    _return = True
                else:  # same color, invalid move
                    raise CBSameColorE('invalid, piece on target coordinates has same color')

        return _return

    def init(self):
        self._init_board()
