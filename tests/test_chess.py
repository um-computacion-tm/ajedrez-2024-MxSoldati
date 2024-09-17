import unittest
from game.board import Board
from game.chess import Chess
from game.exceptions import InvalidMove , EmptyPosition , InvalidTurn


class TestChess(unittest.TestCase):

    def test_is_playing(self):
        self.chess = Chess()
        self.assertTrue(self.chess.is_playing())

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
        self.assertEqual(str(context.exception), "Movimiento de pieza invalido")

        with self.assertRaises(InvalidMove) as context:
            chess.validate_coords(0, 'hola')
        self.assertEqual(str(context.exception), "Movimiento de pieza invalido")

    # por si se mueve una 'pieza' donde esta vacio en esa posicion
    def test_move_empty_position(self):
        chess = Chess()
        with self.assertRaises(EmptyPosition) as context:
            chess.move(2, 2, 0, 1)
        self.assertEqual(str(context.exception), "La posicion esta vacia")

    # por si se mueve una pieza de un jugador que no es el turno
    def test_move_invalid_turn(self):
        chess = Chess()
        with self.assertRaises(InvalidTurn) as context:
            chess.move(1, 0, 2, 0)
        self.assertEqual(str(context.exception), "No puedes mover pieza de otro jugador")

    # por si se mueve una pieza a una posicion invalida
    def test_move_invalid_move(self):
        chess = Chess()
        with self.assertRaises(InvalidMove) as context:
            chess.move(6, 0, 3, 0)  
        self.assertEqual(str(context.exception), "Movimiento de pieza invalido")

    def test_move_valid(self):
        chess = Chess()
        chess.move(7, 1, 5, 2)  # Mover caballo

        self.assertEqual(
            str(chess.show_board()), 
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "  ♞     \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜ ♝♛♚♝♞♜\n"
            )
        )

        chess.move(1, 6, 3, 6)
        self.assertEqual(
            str(chess.show_board()), 
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙ ♙\n"
                "        \n"
                "      ♙ \n"
                "        \n"
                "  ♞     \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜ ♝♛♚♝♞♜\n"
            )
        )

        chess.move(6, 3, 4, 3)
        self.assertEqual(
            str(chess.show_board()), 
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙ ♙\n"
                "        \n"
                "      ♙ \n"
                "   ♟    \n"
                "  ♞     \n"
                "♟♟♟ ♟♟♟♟\n"
                "♜ ♝♛♚♝♞♜\n"
            )
        )

        chess.move(0, 5, 2, 7)
        self.assertEqual(
            str(chess.show_board()), 
            (
                "♖♘♗♕♔ ♘♖\n"
                "♙♙♙♙♙♙ ♙\n"
                "       ♗\n"
                "      ♙ \n"
                "   ♟    \n"
                "  ♞     \n"
                "♟♟♟ ♟♟♟♟\n"
                "♜ ♝♛♚♝♞♜\n"
            )
        )



if __name__ == '__main__':
    unittest.main()