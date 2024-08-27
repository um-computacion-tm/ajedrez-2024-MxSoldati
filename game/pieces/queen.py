from .piece import Piece

class Queen(Piece):
    white_str = "♛"
    black_str = "♕"


#class Queen(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "QUEEN")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♛"
#        else:
#            return "♕"