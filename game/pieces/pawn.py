from .piece import Piece
from ..movements import PiceMovements

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if self.__color__ == "WHITE":
            possible_positions = self.possible_positions_pawn_white(from_row, from_col)
        else:
            possible_positions = self.possible_positions_pawn_black(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_positions(self, row, col):
        if self.__color__ == "WHITE":
            return self.possible_positions_pawn_white(row, col)
        else:
            return self.possible_positions_pawn_black(row, col)

        
        
   