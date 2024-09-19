import unittest
from game.pieces import Rook , Pawn , King , Queen , Knight
from game.movements import PiceMovements
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

    def test_promote_white(self):
        # import ipdb; ipdb.set_trace()
        # instanciamos al peon
        board = Board(for_test=True)
        pawn = Pawn(color='WHITE', board=board)

        # buscamos mover al peon
        board.set_piece(1, 3, pawn)
        board.move(1, 3, 0, 3)

        # AHORA CAMBIAR PEON A REINA
        board.change_piece(0, 3, pawn)

        self.assertIsInstance(
            board.get_piece(0, 3),
            Queen,
        )


    def test_pawn_promotion_black(self):
        board = Board(for_test=True)
        pawn = Pawn(color='BLACK', board=board)

        # buscamos mover al peon
        board.set_piece(6, 2, pawn)
        board.move(6, 2, 7, 2)

        # AHORA CAMBIAR PEON A REINA
        board.change_piece(7, 2, pawn)
        self.assertIsInstance(
            board.get_piece(7, 2),
            Queen,
        )

    # def test_no_promotion(self):
    #     Board = Board(for_test=True)
    #     pawn = Pawn("WHITE", self.board)
    #     self.board.set_piece(2, 0, pawn)
    #     self.board.change_piece(2, 0, pawn)
    #     piece = self.board.get_piece(2, 0)
    #     self.assertIsInstance(piece, Pawn)
    #     self.assertEqual(piece.__color__, "WHITE")
  
    

if __name__ == '__main__':
    unittest.main() 