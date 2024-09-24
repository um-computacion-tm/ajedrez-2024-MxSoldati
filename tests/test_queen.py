import unittest
from game.board import Board
from game.pieces import Queen
from game.pieces import Pawn
class TestQueen(unittest.TestCase):

    

    def test_str(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        self.assertEqual(
            str(queen),
            "♛",
        )

    def test_move_vertical_up(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_vertical_up(4, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (6, 4), (7, 4)]
        )

    def test_move_vertical_up_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(2, 4, queen)
        board.set_piece(4, 4, Pawn("WHITE", board))
        possibles = queen.movement_vertical_up(2, 4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    def test_move_vertical_up_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(1, 4, queen)
        board.set_piece(3, 4, Pawn("BLACK", board))
        possibles = queen.movement_vertical_up(1, 4)
        self.assertEqual(
            possibles,
            [(2, 4), (3, 4)]
        )

    def test_move_vertical_down(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_vertical_down(4, 4)
        self.assertEqual(
            possibles,
            [(3, 4), (2, 4), (1, 4), (0, 4)]
        )

    def test_move_vertical_down_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(6, 4, queen)
        board.set_piece(2, 4, Pawn("WHITE", board))
        possibles = queen.movement_vertical_down(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4), (3, 4)]
        )

    def test_move_vertical_down_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(6, 4, queen)
        board.set_piece(2, 4, Pawn("BLACK", board))
        possibles = queen.movement_vertical_down(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4), (3, 4), (2, 4)]
        )

    def test_move_horizontal_right(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_right_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(4, 6, Pawn("WHITE", board))
        possibles = queen.movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontal_right_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(4, 6, Pawn("BLACK", board))
        possibles = queen.movement_horizontal_right(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6)]
        )

    def test_move_horizontal_left(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontal_left_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(4, 2, Pawn("WHITE", board))
        possibles = queen.movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontal_left_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(4, 2, Pawn("BLACK", board))
        possibles = queen.movement_horizontal_left(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2)]
        )

    def test_move_diagonal_up_left(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_up_left_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(6, 2, Pawn("WHITE", board))
        possibles = queen.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )

    def test_move_diagonal_up_left_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(6, 2, Pawn("BLACK", board))
        possibles = queen.movement_diagonal_up_left(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2)]
        )

    def test_move_diagonal_up_right(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]
        )

    def test_move_diagonal_up_right_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(6, 6, Pawn("WHITE", board))
        possibles = queen.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

    def test_move_diagonal_up_right_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(6, 6, Pawn("BLACK", board))
        possibles = queen.movement_diagonal_up_right(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6)]
        )

    def test_move_diagonal_down_right(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]
        )

    def test_move_diagonal_down_right_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(2, 6, Pawn("WHITE", board))
        possibles = queen.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_move_diagonal_down_right_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(2, 6, Pawn("BLACK", board))
        possibles = queen.movement_diagonal_down_right(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6)]
        )

    def test_move_diagonal_down_left(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        possibles = queen.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1), (0, 0)]
        )

    def test_move_diagonal_down_left_with_obstacle(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(2, 2, Pawn("WHITE", board))
        possibles = queen.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )

    def test_move_diagonal_down_left_attack(self):
        board = Board(for_test=True)
        queen = Queen("WHITE", board)
        board.set_piece(4, 4, queen)
        board.set_piece(2, 2, Pawn("BLACK", board))
        possibles = queen.movement_diagonal_down_left(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2)]
        )

    def test_invalid_move(self):
        board = Board(for_test=True)
        board.set_piece(4, 4, Queen("WHITE", board))  
        queen = board.get_piece(4, 4)  
        is_possible = queen.valid_positions(
            from_row=4,
            from_col=4,
            to_row=5,
            to_col=2,
        )
        self.assertFalse(is_possible)

if __name__ == '__main__':
    unittest.main()