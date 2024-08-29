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
        
    # hay que definir que se mueva, el primer movimiento dos para adelante o uno,
    # y si se puede comer en diagonal y si llega al final del tablero se convierte en reina.
    #def possible_positions_vd(self, row, col):
    #    possibles = []
    #    for next_row in range(row +1, 8): #range(inicio, fin que no esta incluido)
    #        possibles.append((next_row, col))
    #    return possibles
    # ahora, para el peon hay que llamar la funcion que le da los posibles movimientos,
    #  y decir que solamente si es el primer movimiento puede mover dos casillas o una. 
    # y si es el segundo pueda mover solamente una posicion



    #class Pawn(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "PAWN")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♟"
#        else:
#            return "♙"


