from game.board import Board
from game.exceptions import InvalidMove

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col,):

        # validate coords
        self.validate_coords(from_row, from_col)
        self.validate_coords(to_row, to_col)

        # validate move
        piece = self.__board__.get_piece(from_row, from_col)
        if piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        piece = self.__board__.get_piece(to_row, to_col) 
        self.change_turn()


    def validate_coords(self, row, col):
        if type(row) is not int or type(col) is not int:
            raise InvalidMove(f"Invalid coordinates: ({row}, {col})")
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise InvalidMove(f"Invalid coordinates: ({row}, {col})")
        return True
        #faltan los test de esta funcion
        #hacerlo funcionar en el cli

        
    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"