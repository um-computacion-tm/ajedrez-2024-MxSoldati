import unittest
from rook import Rook
from board import Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertIsNone(board.get_piece(0, 1))
        self.assertEqual(board.get_piece(2,2), None)


if __name__ == '__main__':
    unittest.main()