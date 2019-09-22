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


class PieceAbsVector(unittest.TestCase):

    def test_abs_vector(self):
        self.assertEqual([0, 5], Piece._abs_vector([0, -5]))
        self.assertEqual([0, 5], Piece._abs_vector([0, 5]))
        self.assertEqual([1, 1], Piece._abs_vector([-1, -1]))
        self.assertEqual([0, 0], Piece._abs_vector([0, 0]))


class PieceUnifyVector(unittest.TestCase):

    def test_unify_vector_straight(self):

        # single one step vectors, do not handle them
        self.assertEqual([0, 0], Piece._unify_vector([0, 0]))
        self.assertEqual([1, 1], Piece._unify_vector([1, 1]))
        self.assertEqual([1, -1], Piece._unify_vector([1, -1]))

        # allowed vector for a queen or bishop
        self.assertEqual([-1, 1], Piece._unify_vector([-2, 2]))
        self.assertEqual([1, 1], Piece._unify_vector([4, 4]))

        # allowed vector for a knight, kind of a special case
        self.assertEqual([1, -2], Piece._unify_vector([1, -2]))
        self.assertEqual([1, 2], Piece._unify_vector([1, 2]))

        # allowed vector for a rock, queen
        self.assertEqual([0, -1], Piece._unify_vector([0, -5]))
        self.assertEqual([1, 0], Piece._unify_vector([5, 0]))


class PieceRock(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Rock('w')

    def test_rock_validate_vector(self):

        # unified vectors
        self.assertTrue(self.p.validate_vector([0, 1]))
        self.assertTrue(self.p.validate_vector([1, 0]))
        self.assertTrue(self.p.validate_vector([-1, 0]))
        self.assertTrue(self.p.validate_vector([0, -1]))

        # valid vectors
        self.assertTrue(self.p.validate_vector([0, -5]))
        self.assertTrue(self.p.validate_vector([5, 0]))

        # invalid directions
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
        self.assertFalse(self.k.validate_vector([1, 3]))
        self.assertTrue(self.k.validate_vector([1, 2]))
        self.assertTrue(self.k.validate_vector([2, 1]))
        self.assertTrue(self.k.validate_vector([1, -2]))


if __name__ == '__main__':
    unittest.main()
