from board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"     # Blanco(0,str,True) o Negro(1,str,False). Se elije por explicidad

    def move(self, from_row, from_col, to_row, to_col):
        # validate coords        
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"