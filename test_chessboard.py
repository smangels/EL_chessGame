import unittest
from chessboard import ChessBoard


class TestCaseStaticFunctions(unittest.TestCase):
    def test_get_vector_static_function(self):

        self.assertEqual({0, 0}, ChessBoard._get_vector([4, 5], [4, 5]), 'expected NULL vector')
        self.assertEqual({0, 1}, ChessBoard._get_vector([0, 0], [0, 1]), 'expected positive X')
        self.assertEqual({0, -1}, ChessBoard._get_vector([0, 1], [0, 0]), 'expected negative Y')
        self.assertEqual({1, 1}, ChessBoard._get_vector([4, 5], [5, 6]), 'expected ')
        self.assertEqual({-1, -1}, ChessBoard._get_vector([4, 5], [3, 4]), 'expected both negative')
        self.assertEqual({-7, -7}, ChessBoard._get_vector([7, 7], [0, 0]), 'expected negative in both')
        self.assertEqual({1, 2}, ChessBoard._get_vector([1, 2], [2, 4]), 'expected negative in both')
        self.assertEqual({0, 5}, ChessBoard._get_vector([1, 2], [1, 7]), 'expected negative in both')

    def test_coordinate_to_index(self):

        self.assertEqual({0, 7}, ChessBoard._coord_to_index('a1'))
        self.assertEqual({0, 6}, ChessBoard._coord_to_index('a2'))
        self.assertEqual({0, 7}, ChessBoard._coord_to_index('a1'))
        self.assertEqual({0, 7}, ChessBoard._coord_to_index('A1'))
        self.assertEqual({7, 0}, ChessBoard._coord_to_index('h8'))
        with self.assertRaises(NameError):
            ChessBoard._coord_to_index('g9')


# class TestCaseChessBoardMove(unittest.TestCase):
#
#     def test_Move(self):
#         b = ChessBoard()
#         self.assertFalse(b.move('a3', 'a4'))
#         self.assertEqual(b.moves, 0)


if __name__ == '__main__':
    unittest.main()
