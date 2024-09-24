import unittest
from game.pieces import Rook , Pawn , King , Queen , Knight

from game.exceptions import OutOfBoard
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

    def test_get_piece(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.__color__, 'BLACK')

        piece = board.get_piece(7, 7)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.__color__, 'WHITE')

    def test_get_piece_color(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertEqual(piece.__color__, 'BLACK')

        piece = board.get_piece(7, 7)
        self.assertEqual(piece.__color__, 'WHITE')

    def test_not_get_piece(self):
        board = Board()
        piece = board.get_piece(2, 2)
        self.assertEqual(piece, None)

    def test_invalid_position(self):
        board = Board()
        with self.assertRaises(Exception):
            board.get_piece(8, 8)

    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=0,
            to_col=1,
        )

        self.assertIsInstance(
            board.get_piece(0, 1),
            Rook,
        )

        self.assertEqual(
            str(board),
            (
                " ♖      \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
        )

    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

if __name__ == '__main__':
    unittest.main() 