import unittest
from game.board import Board
from game.pieces.bishop import Bishop
from game.pieces.pawn import Pawn

class TestBishop(unittest.TestCase):

    def test_str(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♝",
        )

    def test_move_diagonal_up_left(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_up_left_with_obstacle(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(6, 2, Pawn("WHITE", board))
        possibles = bishop.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )

    def test_move_diagonal_up_left_attack(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(6, 2, Pawn("BLACK", board))
        possibles = bishop.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2)]
        )

    def test_move_diagonal_up_right(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]
        )

    def test_move_diagonal_up_right_with_obstacle(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(6, 6, Pawn("WHITE", board))
        possibles = bishop.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_move_diagonal_up_right_attack(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(6, 6, Pawn("BLACK", board))
        possibles = bishop.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6)]
        )

    def test_move_diagonal_down_right(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]
        )

    def test_move_diagonal_down_right_with_obstacle(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 6, Pawn("WHITE", board))
        possibles = bishop.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_move_diagonal_down_right_attack(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 6, Pawn("BLACK", board))
        possibles = bishop.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6)]
        )

    def test_move_diagonal_down_left(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        possibles = bishop.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1), (0, 0)]
        )

    def test_move_diagonal_down_left_with_obstacle(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 2, Pawn("WHITE", board))
        possibles = bishop.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )

    def test_move_diagonal_down_left_attack(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 2, Pawn("BLACK", board))
        possibles = bishop.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2)]
        )

    def test_invalid_move_straight(self):
        board = Board(for_test=True)
        board.set_piece(4, 4, Bishop("WHITE", board))  
        bishop = board.get_piece(4, 4)  
        is_possible = bishop.valid_positions(
            from_row=4,
            from_col=4,
            to_row=4,
            to_col=5,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()