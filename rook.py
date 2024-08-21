class Pieces:
    def __init__(self, color, name):
        self.__color__ = color  # Cambiado a color
        self.__name__ = name

class Rook(Pieces):
    def __init__(self, color):
        super().__init__(color, "ROOK")

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

class Pawn(Pieces):
    def __init__(self, color):
        super().__init__(color, "PAWN")
        
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"