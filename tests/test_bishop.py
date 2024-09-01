import unittest
from game.board import Board
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
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]  # Assuming the bishop can move diagonally up-right
        )

    def test_move_diagonal_up_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]  # Assuming the bishop can move diagonally up-left
        )

    def test_move_diagonal_down_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]  # Assuming the bishop can move diagonally down-right
        )

    def test_move_diagonal_down_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1)]  # Assuming the bishop can move diagonally down-left
        )

if __name__ == '__main__':
    unittest.main()