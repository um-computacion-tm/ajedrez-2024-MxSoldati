import unittest
from game.board import Board
from game.pieces.king import King
from game.pieces.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        for row in range(8):
            for col in range(8):
                self.board.set_piece(row, col, None)

    def test_str(self):
        board = Board()
        king = King("WHITE", self.board)
        self.assertEqual(
            str(king),
            "♚",
        )

    # verticales -----------------------------------------------------

    def test_move_vertically_up(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_vertical_up(4, 4)
        self.assertEqual(
            possibles,
            [(5, 4)]
        )

    def test_move_vertically_up_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))
        possibles = king.possible_movement_vertical_up(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_vertically_up_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 1, king)
        self.board.set_piece(5, 1, Pawn("BLACK", self.board))
        possibles = king.possible_movement_vertical_up(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertically_down(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_vertical_down(4, 4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    def test_move_vertically_down_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(3, 4, Pawn("WHITE", self.board))
        possibles = king.possible_movement_vertical_down(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_vertically_down_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(3, 4, Pawn("BLACK", self.board))
        possibles = king.possible_movement_vertical_down(4, 4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    # Horizontales -----------------------------------------------------
    
    def test_move_horizontally_left(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontally_left_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(4, 3, Pawn("WHITE", self.board))
        possibles = king.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_horizontally_left_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(4, 3, Pawn("BLACK", self.board))
        possibles = king.possible_movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontally_right(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )
    
    def test_move_horizontally_right_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(4, 5, Pawn("WHITE", self.board))
        possibles = king.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            []
        )
    
    def test_move_horizontally_right_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(4, 5, Pawn("BLACK", self.board))
        possibles = king.possible_movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )


    # Diagonales para abajo  ----------------------------------------------

    def test_move_diagonally_down_left(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )

    def test_move_diagonally_down_left_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(3, 3, Pawn("WHITE", self.board))
        possibles = king.possible_movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_diagonally_down_left_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(3, 3, Pawn("BLACK", self.board))
        possibles = king.possible_movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )

    def test_move_diagonally_down_right(self):
        king = King("WHITE", self.board)
        self.board.set_piece(1, 1, king)
        possibles = king.possible_movement_diagonal_down_right(1, 1)
        self.assertEqual(
            possibles,
            [(0, 2)]
        )

    def test_move_diagonally_down_right_with_obstacle(self):
         king = King("WHITE", self.board)
         self.board.set_piece(4, 4, king)
         self.board.set_piece(3, 5, Pawn("WHITE", self.board))
         possibles = king.possible_movement_diagonal_down_right(4, 4)
         self.assertEqual(
             possibles,
             []
         )

    def test_move_diagonally_down_right_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(3, 5, Pawn("BLACK", self.board))
        possibles = king.possible_movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    # Diagonales para arriba  ----------------------------------------------

    def test_move_diagonally_up_left(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )

    def test_move_diagonally_up_left_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 3, Pawn("WHITE", self.board))
        possibles = king.possible_movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_diagonally_up_left_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 3, Pawn("BLACK", self.board))
        possibles = king.possible_movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )

    def test_move_diagonally_up_right(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.possible_movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_move_diagonally_up_right_with_obstacle(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, Pawn("WHITE", self.board))
        possibles = king.possible_movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_diagonally_up_right_attack(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, Pawn("BLACK", self.board))
        possibles = king.possible_movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_invalid_move_diagonally(self):
        self.board.set_piece(0, 0, King("WHITE", self.board))  # Colocar una torre en la posición (0, 0)
        king = self.board.get_piece(0, 0)  # Obtener la torre en la posición inicial
        is_possible = king.valid_positions(
            from_row=0,
            from_col=0,
            to_row=2,
            to_col=2,
        )
        self.assertFalse(is_possible)
        
if __name__ == '__main__':
    unittest.main()