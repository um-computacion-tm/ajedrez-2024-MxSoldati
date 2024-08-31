import unittest
from game.chess import Chess , InvalidMove


class TestChess(unittest.TestCase):

    def test_validate_coords_valid(self):
        chess = Chess()
        self.assertTrue(chess.validate_coords(0, 0))
        self.assertTrue(chess.validate_coords(7, 7))

    def test_validate_coords_invalid(self):
        chess = Chess()
        
        # -1
        with self.assertRaises(InvalidMove):
            chess.validate_coords(-1, 0)

        # 8
        with self.assertRaises(InvalidMove):
            chess.validate_coords(8, 8)

        # 'hola'
        with self.assertRaises(InvalidMove):
            chess.validate_coords(0, 'hola')


if __name__ == '__main__':
    unittest.main()