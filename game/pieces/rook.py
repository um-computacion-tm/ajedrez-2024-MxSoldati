from .piece import Piece
from ..movements import PiceMovements

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.movement_vertical_desc(from_row, from_col) +
            self.movement_vertical_asc(from_row, from_col) +
            self.movement_horizontal_right(from_row, from_col) +
            self.movement_horizontal_left(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def movement_vertical_desc(self, row, col):
        return PiceMovements.movement_vertical_desc(self, row, col)
    
    def movement_vertical_asc(self, row, col):
        return PiceMovements.movement_vertical_asc(self, row, col)
    
    def movement_horizontal_right(self, row, col):
        return PiceMovements.movement_horizontal_right(self, row, col)
    
    def movement_horizontal_left(self, row, col):
        return PiceMovements.movement_horizontal_left(self, row, col)