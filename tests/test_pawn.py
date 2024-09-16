import unittest
from game.board import Board
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()  
        for row in range(8):
            for col in range(8):
                self.board.set_piece(row, col, None)

    def test_str(self):
        board = Board()
        pawn = Pawn("WHITE", self.board)
        self.assertEqual(
            str(pawn),
            "♟",
        )

    # Blancos

    def test_move_white_initial(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(6, 0)
        self.assertEqual(
            possibles,
            [(5, 0), (4, 0)]  
        )

    def test_move_white_not_initial(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(4, 2)
        self.assertEqual(
            possibles,
            [(3, 2)]  
        )

    def test_move_white_initial_block_other_color(self):
        board = Board()
        board.set_piece(4, 0, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(6, 0)
        self.assertEqual(
            possibles,
            [(5,0)]  
        )

    def test_move_white_not_initial_block_other_color(self):
        board = Board()
        board.set_piece(3, 2, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(4, 2)
        self.assertEqual(
            possibles,
            []  
        )


    def test_move_white_not_initial_block(self):
        board = Board()
        board.set_piece(3, 2, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(4, 2)
        self.assertEqual(
            possibles,
            []  
        )

    def test_move_white_initial_block(self):
        board = Board()
        board.set_piece(4, 0, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(6, 0)
        self.assertEqual(
            possibles,
            [(5, 0)]  
        )

    def test_move_white_not_initial_block(self):
        board = Board()
        board.set_piece(3, 2, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_movement_vertical_up_and_down(4, 2)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_white_attack_right(self):
        board = Board()
        board.set_piece(5, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_attack_diagonal_down_right(6, 0)
        self.assertEqual(
            possibles,
            [(5, 1)]  
        )

    def test_move_white_attack_left(self):
        board = Board()
        board.set_piece(5, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_attack_diagonal_down_left(6, 2)
        self.assertEqual(
            possibles,
            [(5, 1)]  
        )

    def test_move_white_not_attack_right(self):
        board = Board()
        board.set_piece(5, 1, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_attack_diagonal_down_right(6, 0)
        self.assertEqual(
            possibles,
            []  
        )

    def test_move_white_not_attack_left(self):
        board = Board()
        board.set_piece(5, 1, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_attack_diagonal_down_left(6, 2)
        self.assertEqual(
            possibles,
            []  
        )

    # # Negros

    def test_move_black_initial(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0), (3, 0)]  
        )

    def test_move_black_not_initial(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(2, 2)
        self.assertEqual(
            possibles,
            [(3, 2)]  
        )

    def test_move_black_not_initial_block(self):
        board = Board()
        board.set_piece(3, 2, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(2, 2)
        self.assertEqual(
            possibles,
            []  
        )
    
    def test_move_black_initial_block(self):
        board = Board()
        board.set_piece(3, 0, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0)]  
        )

    def test_move_black_not_initial_block_other_color(self):
        board = Board()
        board.set_piece(3, 2, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(2, 2)
        self.assertEqual(
            possibles,
            []  
        )

    def test_move_black_initial_block_other_color(self):
        board = Board()
        board.set_piece(3, 0, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_movement_vertical_up_and_down(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0)]  
        )

    def test_move_black_attack_right(self):
        board = Board()
        board.set_piece(3, 1, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_attack_diagonal_up_right(2, 0)
        self.assertEqual(
            possibles,
            [(3, 1)]  
        )

    def test_move_black_attack_left(self):
        board = Board()
        board.set_piece(3, 6, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_attack_diagonal_up_left(2, 7)
        self.assertEqual(
            possibles,
            [(3, 6)]  
       )
    
    def test_move_black_not_attack_right(self):
        board = Board()
        board.set_piece(3, 1, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_attack_diagonal_up_right(2, 0)
        self.assertEqual(
            possibles,
            []  
        )
    
    def test_move_black_not_attack_left(self):
        board = Board()
        board.set_piece(3, 6, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_attack_diagonal_up_left(2, 7)
        self.assertEqual(
            possibles,
            []
        )
        
    def test_invalid_move_white(self):

        self.board.set_piece(6, 1, Pawn("WHITE", self.board))  
        pawn = self.board.get_piece(6, 1)  
        is_possible = pawn.valid_positions(
            from_row=6,
            from_col=1,
            to_row=7,
            to_col=1,
        )
        self.assertFalse(is_possible)

    def test_invalid_move_black(self):


        self.board.set_piece(1, 1, Pawn("BLACK", self.board))  
        pawn = self.board.get_piece(1, 1)  
        is_possible = pawn.valid_positions(
            from_row=1,
            from_col=1,
            to_row=2,
            to_col=2,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()