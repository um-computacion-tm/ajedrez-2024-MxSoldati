import unittest
from game.chess import Chess
from game.exceptions import InvalidMove


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

    # Me probe para hacer este test que lo hizo walter y me parecio muy prolijo
    def test_invalid_move_exception_message(self):
        chess = Chess()
        with self.assertRaises(InvalidMove) as context:
            chess.validate_coords(8, 8)
        self.assertEqual(str(context.exception), "Movimieto de pieza invalido")

        with self.assertRaises(InvalidMove) as context:
            chess.validate_coords(0, 'hola')
        self.assertEqual(str(context.exception), "Movimieto de pieza invalido")


if __name__ == '__main__':
    unittest.main()