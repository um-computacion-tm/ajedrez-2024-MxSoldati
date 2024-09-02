from .piece import Piece
from ..movements import PiceMovements
class Queen(Piece):
    white_str = "♛"
    black_str = "♕"

    #rectas
    def possible_positions_vd(self, row, col):
        return PiceMovements.movement_vertical_desc(row, col)
    
    def possible_positions_va(self, row, col):
        return PiceMovements.movement_vertical_asc(row, col)
    
    def possible_positions_hr(self, row, col):
        return PiceMovements.movement_horizontal_right(row, col)
    
    def possible_positions_hl(self, row, col):
        return PiceMovements.movement_horizontal_left(row, col)
    
    #diagonales
    def possible_positions_dd(self, row, col):
        return PiceMovements.movement_diagonal_desc(row, col)
    
    def possible_positions_da(self, row, col):
        return PiceMovements.movement_diagonal_asc(row, col)
    
    


#class Queen(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "QUEEN")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♛"
#        else:
#            return "♕"