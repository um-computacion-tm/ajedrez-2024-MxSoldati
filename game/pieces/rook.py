from .piece import Piece
from ..movements import PiceMovements
class Rook(Piece):
    white_str = "♜"
    black_str = "♖"



    def possible_positions_vd(self, row, col):
        return PiceMovements.movment_vertical_desc(row, col)
    
    def possible_positions_va(self, row, col):
        return PiceMovements.movment_vertical_asc(row, col)
    #definir una fucnion que llame de movment.py
    #en movment.py va haber possible_positions, como possible_positions_vertical_asc,possible_positions_vertical_desc,
    #entre otros posibles movment.
    #aca llamariamos los movment posible de la torre.




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


