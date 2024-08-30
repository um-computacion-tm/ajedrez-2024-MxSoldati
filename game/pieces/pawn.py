from .piece import Piece
from ..movements import PiceMovements

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def possible_positions(self, row, col):
        if self.__color__ == "WHITE":
            return PiceMovements.movement_pawn_white(row, col)
        elif self.__color__ == "BLACK":
            return PiceMovements.movement_pawn_black(row, col)
        
   



    #class Pawn(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "PAWN")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♟"
#        else:
#            return "♙"


