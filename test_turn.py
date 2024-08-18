import unittest
from chess import Chess

class TestTurn(unittest.TestCase):
    def test_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "WHITE")
        chess.change_turn()
        self.assertEqual(chess.turn, "BLACK")
        chess.change_turn()
        self.assertEqual(chess.turn, "WHITE")
        chess.change_turn()
        self.assertEqual(chess.turn, "BLACK")
      # Assuming White starts first

if __name__ == '__main__':
    unittest.main()