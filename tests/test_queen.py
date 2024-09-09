import unittest
from game.board import Board
from game.pieces import Queen
from game.pieces import Pawn
class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Esto lo hice para que las piezas con el tablero inicial 
        for row in range(8):  # no me molesten al momento de hacer las pruebas de movimientos
            for col in range(8):
                self.board.set_piece(row, col, None)

    def test_str(self):
        queen = Queen("WHITE", self.board)
        self.assertEqual(
            str(queen),
            "♛",
        )

    def test_move_vertical_up(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_movement_vertical_up(4, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (6, 4), (7, 4)]
        )

    def test_move_vertical_up_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(2, 4, queen)
        self.board.set_piece(4, 4, Pawn("WHITE", self.board))
        possibles = queen.possible_movement_vertical_up(2, 4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    def test_move_vertical_up_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(1, 4, queen)
        self.board.set_piece(3, 4, Pawn("BLACK", self.board))
        possibles = queen.possible_movement_vertical_up(1, 4)
        self.assertEqual(
            possibles,
            [(2, 4), (3, 4)]
        )

    def test_move_vertical_down(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_movement_vertical_down(4, 4)
        self.assertEqual(
            possibles,
            [(3, 4), (2, 4), (1, 4), (0, 4)]
        )

    def test_move_vertical_down_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(6, 4, queen)
        self.board.set_piece(2, 4, Pawn("WHITE", self.board))
        possibles = queen.possible_movement_vertical_down(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4), (3, 4)]
        )

    def test_move_vertical_down_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(6, 4, queen)
        self.board.set_piece(2, 4, Pawn("BLACK", self.board))
        possibles = queen.possible_movement_vertical_down(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4), (3, 4), (2, 4)]
        )

    def test_move_horizontal_right(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_right_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(4, 6, Pawn("WHITE", self.board))
        possibles = queen.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontal_right_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(4, 6, Pawn("BLACK", self.board))
        possibles = queen.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6)]
        )

    def test_move_horizontal_left(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontal_left_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(4, 2, Pawn("WHITE", self.board))
        possibles = queen.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontal_left_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(4, 2, Pawn("BLACK", self.board))
        possibles = queen.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2)]
        )

    def test_move_diagonal_up_left(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_up_left_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(6, 2, Pawn("WHITE", self.board))
        possibles = queen.possible_positions_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )

    def test_move_diagonal_up_left_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(6, 2, Pawn("BLACK", self.board))
        possibles = queen.possible_positions_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2)]
        )

    def test_move_diagonal_up_right(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]
        )

    def test_move_diagonal_up_right_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(6, 6, Pawn("WHITE", self.board))
        possibles = queen.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_move_diagonal_up_right_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(6, 6, Pawn("BLACK", self.board))
        possibles = queen.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6)]
        )

    def test_move_diagonal_down_right(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]
        )

    def test_move_diagonal_down_right_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(2, 6, Pawn("WHITE", self.board))
        possibles = queen.possible_positions_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_move_diagonal_down_right_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(2, 6, Pawn("BLACK", self.board))
        possibles = queen.possible_positions_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6)]
        )

    def test_move_diagonal_down_left(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1), (0, 0)]
        )

    def test_move_diagonal_down_left_with_obstacle(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(2, 2, Pawn("WHITE", self.board))
        possibles = queen.possible_positions_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )

    def test_move_diagonal_down_left_attack(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(2, 2, Pawn("BLACK", self.board))
        possibles = queen.possible_positions_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2)]
        )

    def test_invalid_move(self):
        self.board.set_piece(4, 4, Queen("WHITE", self.board))  
        queen = self.board.get_piece(4, 4)  
        is_possible = queen.valid_positions(
            from_row=4,
            from_col=4,
            to_row=5,
            to_col=2,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()