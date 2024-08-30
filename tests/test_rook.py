import unittest
from game.board import Board
from game.pieces.rook import Rook

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
        possibles = rook.possible_positions_vd(4,0)
        self.assertEqual(
                possibles,
                [(5,0), (6,0), (7,0)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE",  board)
        possibles = rook.possible_positions_va(4,0)
        self.assertEqual(
                possibles,
                [(3,0), (2,0), (1,0), (0,0)]
        )        
    
    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hr(0,4)
        self.assertEqual(
                possibles,
                [(0,5), (0,6), (0,7)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hl(0,4)
        self.assertEqual(
                possibles,
                [(0,3), (0,2), (0,1), (0,0)]
        )


if __name__ == '__main__':
    unittest.main()