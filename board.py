from rook import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):  # Forma de hacer un tablero
            col = []  # la primera recorrida hace las 8 columnas
            for _ in range(8):  # Donde en cada columna tiene sus 8 filas
                col.append(None)
            self.__positions__.append(col)  # Corregido aquí
        self.__positions__[0][0] = Rook('BLACK')  # Black
        self.__positions__[0][7] = Rook('BLACK')
        self.__positions__[7][7] = Rook('WHITE')  # White
        self.__positions__[7][0] = Rook('WHITE')

    def get_piece(self, row, col):
        return self.__positions__[row][col]


