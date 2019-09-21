from enum import Enum
from typing import List


class Color(Enum):
    BLACK = 1
    WHITE = 2

    def __str__(self):
        if self.value == 1:
            return 'b'
        else:
            return 'w'


class Piece(object):
    """implements a base class for pieces in a chess game"""

    PIECE_TYPE_MAP = {
        'K': 'King',
        'Q': 'Queen',
        'r': 'Rock',
        'k': 'Knight',
        'b': 'Bishop',
        'p': 'Pawn'
    }

    def __init__(self, color):
        self.name = None
        self.moves = None
        if color in ['w', 'b']:
            self.color = Color.WHITE if color == 'w' else Color.BLACK
        else:
            raise NameError('invalid color')

    def validate_vector(self, vector: List[int]):
        """validate vector with allowed moves of a certain piece"""
        raise NotImplementedError('base class')

    def __str__(self):
        if self.color == 1:
            _color = 'w'
        else:
            _color = 'b'
        _str = "%s%s" % (self.color, self.name)
        return _str


class Knight(Piece):
    """Implement specialization for Knights"""

    def __init__(self, color):
        super(Knight, self).__init__(color)
        self.name = 'k'
        self.moves = {
            "directions": [[-2, -1], [-2, 1],
                           [-1, -2], [-1, 2],
                           [1, -2], [1, 2],
                           [2, -1], [2, 1]],
            "steps": 1,
            "jump": True
        }

    def validate_vector(self, vector: List[int]):
        return True


class King(Piece):
    """Implement specialization for a king"""
    
    def __init__(self, color):
        super(King, self).__init__(color)
        self.name = 'K'
        self.moves = {
            "directions":  [[-1, -1], [-1, 1], [-1, 0],
                    [1, -1], [1, 1], [1, 0],
                    [0, 1], [0, -1]],
            "steps": None,
            "jump": False
        }

    def validate_vector(self, vector: List[int]):
        pass


class Queen(Piece):
    """Implement specialization for a queen"""

    def __init__(self, color):
        super(Queen, self).__init__(color)
        self.name = 'Q'
        self.moves = {
            "directions":  [[-1, -1], [-1, 1], [-1, 0],
                    [1, -1], [1, 1], [1, 0],
                    [0, 1], [0, -1]],
            "steps": None,
            "jump": False
        }

    def validate_vector(self, vector: List[int]):
        return True


class Rock(Piece):
    """Implement specialization for a rock"""

    def __init__(self, color):
        super(Rock, self).__init__(color)
        self.name = 'r'
        self.moves = {
            "directions": [[-1, 0], [0, 1], [1, 0], [0, -1]],
            "steps": None,
            "jump": False
        }

    def validate_vector(self, vector: List[int]):
        pass


class Bishop(Piece):
    """Implement specialization for a bishop"""
    def __init__(self, color):
        super(Bishop, self).__init__(color)
        self.name = 'b'

        self.moves = {
            "directions": [[-1, 1], [1, 1], [1, -1], [-1,-1]],
            "steps": None,
            "jump": False
        }

    def validate_vector(self, vector: List[int]):
        pass


class Pawn(Piece):
    """Implement specialization for a pawn"""

    def __init__(self, color):
        super(Pawn, self).__init__(color)
        self.name = 'p'
        self.moves = {
            "directions":  [[-1, -1], [-1, 1], [-1, 0],
                            [1, -1], [1, 1], [1, 0],
                            [0, 1], [0, -1]],
            "steps": 1,
            "steps_start": 2,
            "jump": False
        }

    def validate_vector(self, vector: List[int]):
        pass
