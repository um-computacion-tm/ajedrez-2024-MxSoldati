from rook import Rook , Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):  # Forma de hacer un tablero
            col = []  # la primera recorrida hace las 8 columnas
            for _ in range(8):  # Donde en cada columna tiene sus 8 filas
                col.append(None)
            self.__positions__.append(col)  # Corregido aquí
        # Rooks
        self.__positions__[0][0] = Rook('BLACK')  # Black
        self.__positions__[0][7] = Rook('BLACK')
        self.__positions__[7][7] = Rook('WHITE')  # White
        self.__positions__[7][0] = Rook('WHITE')
        
        # Pawns 
        self.__positions__[1][0] = Pawn('BLACK')
        self.__positions__[1][7] = Pawn('BLACK')
        self.__positions__[6][0] = Pawn('WHITE')
        self.__positions__[6][7] = Pawn('WHITE')

    def get_piece(self, row, col):
        if self.__positions__[row][col] == None:
            return None
        return self.__positions__[row][col]


