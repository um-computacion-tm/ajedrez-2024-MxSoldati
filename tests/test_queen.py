import unittest
from game.pieces.queen import Queen
from game.board import Board

class TestQueen(unittest.TestCase):
    def test_str(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(
            str(queen),
            "♛",
        )

    def test_move_vertical_desc(self):
        board = Board()
        queen = Queen("WHITE", board)
        possibles = queen.possible_positions_vd(4,0)
        self.assertEqual(
                possibles,
                [(5,0), (6,0), (7,0)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        queen = Queen("WHITE",  board)
        possibles = queen.possible_positions_va(4,0)
        self.assertEqual(
                possibles,
                [(3,0), (2,0), (1,0), (0,0)]
        )        
    
    def test_move_horizontal_right(self):
        board = Board()
        queen = Queen("WHITE", board)
        possibles = queen.possible_positions_hr(0,4)
        self.assertEqual(
                possibles,
                [(0,5), (0,6), (0,7)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        queen = Queen("WHITE", board)
        possibles = queen.possible_positions_hl(0,4)
        self.assertEqual(
                possibles,
                [(0,3), (0,2), (0,1), (0,0)]
        )

if __name__ == '__main__':
    unittest.main()