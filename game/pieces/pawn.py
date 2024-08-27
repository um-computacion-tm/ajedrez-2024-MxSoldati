from .piece import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    #class Pawn(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "PAWN")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♟"
#        else:
#            return "♙"