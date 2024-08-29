import unittest
from game.board import Board
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_str_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(
            str(pawn),
            "♟",
        )

    def test_str_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        self.assertEqual(
            str(pawn),
            "♙",
        )

    def test_move_white_initial(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(1, 0)
        self.assertEqual(
            possibles,
            [(2, 0), (3, 0)]  # Assuming the pawn can move two steps forward on its first move
        )

    def test_move_black_initial(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(6, 0)
        self.assertEqual(
            possibles,
            [(5, 0), (4, 0)]  # Assuming the pawn can move one step forward
        )

    def test_move_white_not_inital(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions(4, 2)
        self.assertEqual(
            possibles,
            [(5, 2)]  # Assuming the pawn can move one step forward
        )

    def test_move_black_not_inital(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions(4, 2)
        self.assertEqual(
            possibles,
            [(3, 2)]  # Assuming the pawn can move one step forward
        )
if __name__ == '__main__':
    unittest.main()