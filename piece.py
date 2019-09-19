from enum import Enum
import json


class Color(Enum):
    BLACK = 1
    WHITE = 2

    def __str__(self):
        return self.name


class Piece(object):

    PIECE_TYPE_MAP = {
        'K': 'King',
        'q': 'Queen',
        'r': 'Rock',
        'k': 'Knight',
        'b': 'Bishop',
        'p': 'Pawn'
    }

    def __init__(self, color):
        self.name = None
        print('set color %s' % color)
        self.color = Color.WHITE if color == 'w' else Color.BLACK

    def __str__(self):
        if self.color == 1:
            _color = 'w'
        else:
            _color = 'b'
        _str = "%s%s" % (self.color, self.name)
        return _str


class Knight(Piece):

    def __init__(self, color):
        super(Knight, self).__init__(color)
        self.name = 'k'


class King(Piece):
    
    def __init__(self, color):
        super(King, self).__init__(color)
        self.name = 'K'


class Queen(Piece):

    def __init__(self, color):
        super(Queen, self).__init__(color)
        self.name = 'q'


class Rock(Piece):

    def __init__(self, color):
        super(Rock, self).__init__(color)
        self.name = 'r'


class Bishop(Piece):

    def __init__(self, color):
        super(Bishop, self).__init__(color)
        self.name = 'b'


class Pawn(Piece):

    def __init__(self, color):
        super(Pawn, self).__init__(color)
        self.name = 'p'





