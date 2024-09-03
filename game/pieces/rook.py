from .piece import Piece
from ..movements import PiceMovements
class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def valid_positions(
        self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions


    def possible_positions_vd(self, row, col):
        return PiceMovements.movement_vertical_desc(row, col)
    
    def possible_positions_va(self, row, col):
        return PiceMovements.movement_vertical_asc(row, col)
    
    def possible_positions_hr(self, row, col):
        return PiceMovements.movement_horizontal_right(row, col)
    
    def possible_positions_hl(self, row, col):
        return PiceMovements.movement_horizontal_left(row, col)





#        
#
#class Rook(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "ROOK")
#
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♜"
#        else:
#            return "♖"


