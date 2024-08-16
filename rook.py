class Pieces:
    def __init__(self, color):
        self.color = color  # Cambiado a color

class Rook(Pieces):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = 'ROOK'

class Pawn(Pieces):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = 'PAWN'