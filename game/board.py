from .pieces import Rook , Pawn , Bishop , King , Queen , Horse
from .exceptions import OutOfBoard
class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):  # Forma de hacer un tablero
            col = []  # la primera recorrida hace las 8 columnas
            for _ in range(8):  # Donde en cada columna tiene sus 8 filas
                col.append(None)
            self.__positions__.append(col)  # Corregido aquí
        # Rooks
        self.__positions__[0][0] = Rook('BLACK', self)  # Black
        self.__positions__[0][7] = Rook('BLACK', self)
        self.__positions__[7][7] = Rook('WHITE', self)  # White
        self.__positions__[7][0] = Rook('WHITE', self)

        # Horses 
        self.__positions__[0][1] = Horse('BLACK', self)
        self.__positions__[0][6] = Horse('BLACK', self)
        self.__positions__[7][1] = Horse('WHITE', self)
        self.__positions__[7][6] = Horse('WHITE', self)


        # Bishops
        self.__positions__[0][2] = Bishop('BLACK', self)
        self.__positions__[0][5] = Bishop('BLACK', self)
        self.__positions__[7][2] = Bishop('WHITE', self)
        self.__positions__[7][5] = Bishop('WHITE', self)

        # Queens
        self.__positions__[0][3] = Queen('BLACK', self)
        self.__positions__[7][3] = Queen('WHITE', self)

        # Kings
        self.__positions__[0][4] = King('BLACK', self)
        self.__positions__[7][4] = King('WHITE', self)
        
        # Pawns 
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  
            self.__positions__[6][col] = Pawn("WHITE", self)

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
        if not (0 <= row < 8 or 0 <= col < 8):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)