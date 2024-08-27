from game.rook import Rook , Pawn , Bishop , King , Queen , Horse

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

        # Horses 
        self.__positions__[0][1] = Horse('BLACK')
        self.__positions__[0][6] = Horse('BLACK')
        self.__positions__[7][1] = Horse('WHITE')
        self.__positions__[7][6] = Horse('WHITE')


        # Bishops
        self.__positions__[0][2] = Bishop('BLACK')
        self.__positions__[0][5] = Bishop('BLACK')
        self.__positions__[7][2] = Bishop('WHITE')
        self.__positions__[7][5] = Bishop('WHITE')

        # Queens
        self.__positions__[0][3] = Queen('BLACK')
        self.__positions__[7][3] = Queen('WHITE')

        # Kings
        self.__positions__[0][4] = King('BLACK')
        self.__positions__[7][4] = King('WHITE')
        
        # Pawns 
        self.__positions__[1][0] = Pawn('BLACK')
        self.__positions__[1][7] = Pawn('BLACK')
        self.__positions__[1][1] = Pawn('BLACK')
        self.__positions__[1][2] = Pawn('BLACK')
        self.__positions__[1][3] = Pawn('BLACK')
        self.__positions__[1][4] = Pawn('BLACK')
        self.__positions__[1][5] = Pawn('BLACK')
        self.__positions__[1][6] = Pawn('BLACK')
        self.__positions__[1][7] = Pawn('BLACK')


        self.__positions__[6][0] = Pawn('WHITE')
        self.__positions__[6][1] = Pawn('WHITE')
        self.__positions__[6][2] = Pawn('WHITE')
        self.__positions__[6][3] = Pawn('WHITE')
        self.__positions__[6][4] = Pawn('WHITE')
        self.__positions__[6][5] = Pawn('WHITE')
        self.__positions__[6][6] = Pawn('WHITE')
        self.__positions__[6][7] = Pawn('WHITE')

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
        

    def get_piece(self, row, col):
        return self.__positions__[row][col]