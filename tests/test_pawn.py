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

    def test_move_white_initial(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(6, 0)
        self.assertEqual(
            possibles,
            [(5, 0), (4, 0)]  
        )

    def test_move_white_not_inital(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(4, 2)
        self.assertEqual(
            possibles,
            [(3, 2)]  
        )

    def test_move_white_not_inital_blocked(self):
        board = Board()
        board.set_piece(3, 2, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(4, 2)
        self.assertEqual(
            possibles,
            []  
        )

    def test_move_white_initial_blocked(self):
        board = Board()
        board.set_piece(4, 0, Pawn("WHITE", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(6, 0)
        self.assertEqual(
            possibles,
            [(5, 0)]  
        )

    def test_move_white_attack_right(self):
        board = Board()
        board.set_piece(4, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(5, 0)
        self.assertEqual(
            possibles,
            [(4, 1)]  
        )
    
    def test_move_white_attack_left(self):
        board = Board()
        board.set_piece(4, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(5, 2)
        self.assertEqual(
            possibles,
            [(4, 1)]  
        )

    def test_move_black_initial(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0), (3, 0)]  
        )

    def test_move_black_not_inital(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(2, 2)
        self.assertEqual(
            possibles,
            [(3, 2)]  
        )


    def test_move_black_not_inital_blocked(self):
        board = Board()
        board.set_piece(3, 2, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(2, 2)
        self.assertEqual(
            possibles,
            []  
        )
    
    def test_move_black_initial_blocked(self):
        board = Board()
        board.set_piece(3, 0, Pawn("BLACK", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0)]  
        )


    def test_move_black_attack_right(self):
        board = Board()
        board.set_piece(3, 1, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(2, 0)
        self.assertEqual(
            possibles,
            [(3, 1)]  
        )
    
    def test_move_black_attack_left(self):
        board = Board()
        board.set_piece(3, 1, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(2, 2)
        self.assertEqual(
            possibles,
            [(3, 1)]  
        )

if __name__ == '__main__':
    unittest.main()