import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Crear un tablero con las piezas iniciales
        # Limpiar el tablero
        for row in range(8):
            for col in range(8):
                self.board.set_piece(row, col, None)

    def test_str(self):
        rook = Rook("WHITE", self.board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertically_down(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        possibles = rook.possible_movement_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertically_down_with_obstacle(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(2, 1, Pawn("WHITE", self.board))
        possibles = rook.possible_movement_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1)]
        )

    def test_move_vertically_down_attack(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(2, 1, Pawn("BLACK", self.board))
        possibles = rook.possible_movement_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1)]
        )

    def test_move_vertically_up(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        possibles = rook.possible_movement_vertical_up(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertically_up_with_obstacle(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(6, 1, Pawn("WHITE", self.board))
        possibles = rook.possible_movement_vertical_up(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertically_up_attack(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(6, 1, Pawn("BLACK", self.board))
        possibles = rook.possible_movement_vertical_up(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_horizontally_right(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        possibles = rook.possible_movement_horizontal_right(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontally_right_with_obstacle(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(4, 3, Pawn("WHITE", self.board))
        possibles = rook.possible_movement_horizontal_right(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2)]
        )

    def test_move_horizontally_right_attack(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 1, rook)
        self.board.set_piece(4, 3, Pawn("BLACK", self.board))
        possibles = rook.possible_movement_horizontal_right(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3)]
        )

    def test_move_horizontally_left(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 6, rook)
        possibles = rook.possible_movement_horizontal_left(4, 6)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontally_left_with_obstacle(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 6, rook)
        self.board.set_piece(4, 4, Pawn("WHITE", self.board))
        possibles = rook.possible_movement_horizontal_left(4, 6)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontally_left_attack(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 6, rook)
        self.board.set_piece(4, 4, Pawn("BLACK", self.board))
        possibles = rook.possible_movement_horizontal_left(4, 6)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 4)]
        )

    def test_invalid_move_diagonally(self):
        self.board.set_piece(0, 0, Rook("WHITE", self.board))  # Colocar una torre en la posición (0, 0)
        rook = self.board.get_piece(0, 0)  # Obtener la torre en la posición inicial
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()