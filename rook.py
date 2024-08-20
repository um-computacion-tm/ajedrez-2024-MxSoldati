class Pieces:
    def __init__(self, color):
        self.__color__ = color  # Cambiado a color

class Rook(Pieces):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

class Pawn(Pieces):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"