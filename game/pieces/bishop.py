from .piece import Piece
from ..movements import PiceMovements
class Bishop(Piece):
    white_str = "♝"
    black_str = "♗"

    def possible_positions_diagonal_up_left(self, row, col):
        return PiceMovements.possible_positions_diagonal_up_left(row, col)
    
    def possible_positions_diagonal_up_right(self, row, col):
        return PiceMovements.possible_positions_diagonal_up_right(row, col)
    
    def possible_positions_diagonal_down_right(self, row, col):
        return PiceMovements.possible_positions_diagonal_down_right(row, col)
    
    def possible_positions_diagonal_down_left(self, row, col):
        return PiceMovements.possible_positions_diagonal_down_left(row, col)
     