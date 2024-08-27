from .piece import Piece

class Horse(Piece):
    white_str = "♞"
    black_str = "♘"


#class Horse(Pieces):  
#    def __init__(self, color):
#        super().__init__(color, "HORSES")
#        
#    def __str__(self):
#        if self.__color__ == "WHITE":
#            return "♞"
#        else:
#            return "♘"