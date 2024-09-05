import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 0, rook)
        possibles = rook.movement_vertical_desc(4, 0)
        self.assertEqual(
            possibles,
            [(5, 0), (6, 0), (7, 0)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 0, rook)
        possibles = rook.movement_vertical_asc(4, 0)
        self.assertEqual(
            possibles,
            [(3, 0), (2, 0), (1, 0), (0, 0)]
        )

    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 4, rook)
        possibles = rook.movement_horizontal_right(0, 4)
        self.assertEqual(
            possibles,
            [(0, 5), (0, 6), (0, 7)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 4, rook)
        possibles = rook.movement_horizontal_left(0, 4)
        self.assertEqual(
            possibles,
            [(0, 3), (0, 2), (0, 1), (0, 0)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.movement_vertical_desc(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.movement_vertical_desc(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

if __name__ == '__main__':
    unittest.main()