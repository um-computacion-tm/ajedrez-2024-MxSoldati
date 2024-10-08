import unittest
from game.board import Board
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn


class TestKnight(unittest.TestCase):


    def test_str(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        self.assertEqual(
            str(knight),
            "♞",
        )

    def test_move_knight(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(4, 4, knight)
        possibles = knight.possible_positions_knight(4, 3)
        self.assertEqual(
            possibles,
            [(6, 4), (6, 2), (2, 4), (2, 2), (5, 5), (5, 1), (3, 5), (3, 1)]
        )

    def test_move_knight_edge(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(0, 0, knight)
        possibles = knight.possible_positions_knight(0, 0)
        self.assertEqual(
            possibles,
            [(2, 1), (1, 2)]
        )

    def test_move_knight_with_obstacle(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(4, 4, knight)
        board.set_piece(6, 5, Pawn("WHITE", board))
        possibles = knight.possible_positions_knight(4, 4)
        self.assertEqual(
            possibles,
            [(6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        )

    def test_move_knight_attack(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(4, 4, knight)
        board.set_piece(6, 5, Pawn("BLACK", board))
        possibles = knight.possible_positions_knight(4, 4)
        self.assertEqual(
            possibles,
            [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        )


    def test_move_knight_edge_with_obstacle(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(0, 0, knight)
        board.set_piece(2, 1, Pawn("WHITE", board))
        possibles = knight.possible_positions_knight(0, 0)
        self.assertEqual(
            possibles,
            [(1, 2)]
        )

    def test_move_knight_edge_attack(self):
        board = Board(for_test=True)
        knight = Knight("WHITE", board)
        board.set_piece(0, 0, knight)
        board.set_piece(2, 1, Pawn("BLACK", board))
        possibles = knight.possible_positions_knight(0, 0)
        self.assertEqual(
            possibles,
            [(2, 1), (1, 2)]
        )

    def test_invalid_move(self):
        board = Board(for_test=True)
        board.set_piece(0, 0, Knight("WHITE", board))  
        knight = board.get_piece(0, 0) 
        is_possible = knight.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()