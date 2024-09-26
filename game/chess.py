from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn, EmptyPosition, InvalidMove
from game.pieces.pawn import Pawn
from game.pieces.queen import Queen


class Chess:
    def __init__(self):


        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True
    
    def validate_coords(self, row, col):
        if type(row) is int and type(col) is int:
            if 0 <= row < 8 and 0 <= col < 8:
                return True
        raise InvalidMove()
    
    def move(self, from_row, from_col, to_row, to_col,):

        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()

    def change_piece(self, row, col):

        current_piece = self.__board__.get_piece(row, col)
        if isinstance(current_piece, Pawn):
            if (current_piece.__color__ == "WHITE" and row == 0) or (current_piece.__color__ == "BLACK" and row == 7):
                self.__board__.set_piece(row, col, Queen(current_piece.__color__, self.__board__))

    def determine_winner(self):
        white_pieces = 0
        black_pieces = 0
        # En esta funcion solamente queremos tener la info si quedan o no, piezas.
        #asi podemos determinar el ganador.
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece is not None:
                    if piece.__color__ == "WHITE":
                        white_pieces += 1
                    elif piece.__color__ == "BLACK":
                        black_pieces += 1
        if white_pieces == 0:
            return "Black wins"
        elif black_pieces == 0:
            return "White wins"
        else:
            return "No winner yet"
        
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