import unittest
from rook import Rook
from board import Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertIsNone(board.get_piece(0, 1))
        self.assertEqual(board.get_piece(2,2), None)

    def test_get_piece(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertEqual(piece.color, 'BLACK')

        piece = board.get_piece(7, 7)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.color, 'WHITE')


if __name__ == '__main__':
    unittest.main()