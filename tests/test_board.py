import unittest
from game.pieces import Rook , Pawn , Bishop , King , Queen , Horse
from game.board import Board

class TestBoard(unittest.TestCase):
    
    def test_init(self):
        board = Board()
        self.assertIsNone(board.get_piece(3, 1))
        self.assertEqual(board.get_piece(2,2), None)

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )

    def test_get_piece_color(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertEqual(piece.__color__, 'BLACK')

        piece = board.get_piece(7, 7)
        self.assertEqual(piece.__color__, 'WHITE')




if __name__ == '__main__':
    unittest.main()