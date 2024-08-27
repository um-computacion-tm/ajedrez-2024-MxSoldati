from .piece import Piece
class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row +1, 8): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row -1, -1, -1): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles    
    #definir una fucnion que llame de movimientos.py
    #en movimientos.py va haber possible_positions, como possible_positions_vertical_asc,possible_positions_vertical_desc,
    #entre otros posibles movimientos.
    #aca llamariamos los movimientos posible de la torre.




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


