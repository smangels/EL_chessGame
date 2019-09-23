import unittest
from chessboard import ChessBoard
from chessboard import CBSameColorE, CBNothingToMoveE


class TestCaseStaticFunctions(unittest.TestCase):
    def test_get_vector_static_function(self):

        self.assertEqual([0, 0], ChessBoard._get_vector([4, 5], [4, 5]), 'expected NULL vector')
        self.assertEqual([0, 1], ChessBoard._get_vector([0, 0], [0, 1]), 'expected positive X')
        self.assertEqual([0, -1], ChessBoard._get_vector([0, 1], [0, 0]), 'expected negative Y')
        self.assertEqual([1, 1], ChessBoard._get_vector([4, 5], [5, 6]), 'expected ')
        self.assertEqual([-1, -1], ChessBoard._get_vector([4, 5], [3, 4]), 'expected both negative')
        self.assertEqual([-7, -7], ChessBoard._get_vector([7, 7], [0, 0]), 'expected negative in both')
        self.assertEqual([1, 2], ChessBoard._get_vector([1, 2], [2, 4]), 'expected negative in both')
        self.assertEqual([0, 5], ChessBoard._get_vector([1, 2], [1, 7]), 'expected negative in both')

    def test_coordinate_to_index(self):

        self.assertEqual([7, 0], ChessBoard._coord_to_index('a1'))
        self.assertEqual([6, 0], ChessBoard._coord_to_index('a2'))
        self.assertEqual([7, 0], ChessBoard._coord_to_index('a1'))
        self.assertEqual([7, 0], ChessBoard._coord_to_index('A1'))
        self.assertEqual([0, 7], ChessBoard._coord_to_index('h8'))
        with self.assertRaises(NameError):
            ChessBoard._coord_to_index('g9')


class TestCaseCheckPath(unittest.TestCase):

    def test_get_path(self):
        self.b = ChessBoard()

        # check path for a white bishop (C1) -> (E3), blocked by own pawn
        self.assertFalse(self.b._check_path([7, 2], [-1, 1], [5, 4]))

        # move black pawn and later white pawn as well as check path for same knight
        self.b.move('d2', 'd4')
        self.assertTrue(self.b._check_path([7, 2], [-1, 1], [5, 4]))

        # check path for white pawn (C3) -> (C5), no obstacles
        self.assertTrue(self.b._check_path([6, 2], [-1, 0], [4, 2]))


class TestCaseChessBoardMove(unittest.TestCase):

    def setUp(self) -> None:
        self.b = ChessBoard()

    def test_MoveNothingToMove(self):
        with self.assertRaises(CBNothingToMoveE):
            self.b.move('a3', 'a4')
        self.assertEqual(self.b.moves, 0)

    def test_MoveSameColorNoMove(self):
        with self.assertRaises(CBSameColorE):
            self.b.move('a2', 'b2')

    def test_MoveEmptyDestination(self):
        self.assertTrue(self.b.move('a2', 'a4'))

    def tearDown(self) -> None:
        del self.b


if __name__ == '__main__':
    unittest.main()
