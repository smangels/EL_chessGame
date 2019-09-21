import unittest

from piece import Piece, Color, Rock, Knight


class PieceColor(unittest.TestCase):

    def test_PieceColorWhite(self):
        self.p = Piece('w')
        self.assertEqual(self.p.color, Color.WHITE)

    def test_PieceColorWhite(self):
        self.p = Piece('b')
        self.assertEqual(self.p.color, Color.BLACK)

    def test_InvalidPieceColor(self):
        with self.assertRaises(NameError):
            self.p = Piece('p')


class PieceRock(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Rock('w')

    def test_rock_validate_vector(self):
        self.assertTrue(self.p.validate_vector([0, 1]))
        self.assertTrue(self.p.validate_vector([1, 0]))
        self.assertTrue(self.p.validate_vector([-1, 0]))
        self.assertTrue(self.p.validate_vector([0, -1]))
        self.assertFalse(self.p.validate_vector([1, 1]))
        self.assertFalse(self.p.validate_vector([-1, -1]))
        self.assertFalse(self.p.validate_vector([1, -1]))
        self.assertFalse(self.p.validate_vector([-1, 1]))

class PieceKnight(unittest.TestCase):

    def setUp(self) -> None:
        self.k = Knight('b')

    def test_knight_color(self):
        self.assertEqual(self.k.color, Color.BLACK)

    def test_knight_validate_vector(self):
        self.assertFalse(self.k.validate_vector([1, 4]))
        self.assertTrue(self.k.validate_vector([1, 2]))
        self.assertFalse(self.k.validate_vector([1, 3]))
        self.assertTrue(self.k.validate_vector([2, 1]))


if __name__ == '__main__':
    unittest.main()
