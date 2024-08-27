from .piece import Piece

class King(Piece):
    white_str = "♚"
    black_str = "♔"
        

#class King(Pieces):
#    def __init__(self, color):
#        super().__init__(color, "KING")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♚"
#        else:
#            return "♔"