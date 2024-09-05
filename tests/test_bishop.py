import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.bishop import Bishop

class TestBishop(unittest.TestCase):

    def test_str_white(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♝",
        )

    def test_move_diagonal_up_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]  
        )

    def test_move_diagonal_up_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]  
        )

    def test_move_diagonal_down_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]  
        )

    def test_move_diagonal_down_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1), (0, 0)]  
        )

    def test_move_diagonal_up_right_with_own_piece(self):
        board = Board()
        board.set_piece(6, 5, Pawn("WHITE", board))
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_move_diagonal_up_right_with_opponent_piece(self):
        board = Board()
        board.set_piece(6, 6, Pawn("BLACK", board))
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6)]
        )