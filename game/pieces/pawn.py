from .piece import Piece
from ..movements import PiceMovements

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"
    __start_row__ = None

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if self.__color__ == "WHITE":
            possible_positions = (
                self.possible_movement_vertical_up_and_down(from_row, from_col) + 
                self.possible_attack_diagonal(from_row, from_col) 
            )
        else:
            possible_positions = (
                self.possible_movement_vertical_up_and_down(from_row, from_col) +
                self.possible_attack_diagonal(from_row, from_col) 
            )
        return (to_row, to_col) in possible_positions
        
    def possible_movement_vertical_up_and_down(self, row, col):

        if self.__color__ == "WHITE":
            self.__start_row__ = 6
            return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_down)
        else:
            self.__start_row__ = 1
            return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_up)
    

    def possible_movement_vertical(self, row, col, movement_func):

        direction = -1 if movement_func == PiceMovements.movement_vertical_down else 1
        if row == self.__start_row__ and self.__board__.get_piece(row + 2 * direction, col) is None and self.__board__.get_piece(row + 1 * direction, col) is None:
            return [(row + 1 * direction, col), (row + 2 * direction, col)]
        elif self.__board__.get_piece(row + 1 * direction, col) is None:
            return [(row + 1 * direction, col)]
        return []

    def possible_attack_diagonal(self, row, col):
        if self.__color__ == "WHITE":
            return self.possible_attack_diagonal_direction(row, col, -1, -1) + \
                   self.possible_attack_diagonal_direction(row, col, -1, 1)
        else:
            return self.possible_attack_diagonal_direction(row, col, 1, -1) + \
                   self.possible_attack_diagonal_direction(row, col, 1, 1)

    def possible_attack_diagonal_direction(self, row, col, row_offset, col_offset):
        target_row = row + row_offset
        target_col = col + col_offset
        if 0 <= target_row < 8 and 0 <= target_col < 8:
            piece = self.__board__.get_piece(target_row, target_col)
            if piece is not None and piece.__color__ != self.__color__:
                return [(target_row, target_col)]
        return []

    # Falta refactorizarlo
    # def possible_attack_diagonal_down_left(self, row, col):
    #     if self.__board__.get_piece(row - 1, col - 1) is not None and self.__board__.get_piece(row - 1, col - 1).__color__ != self.__color__:
    #         return [(row - 1, col - 1)]
    #     return []
    # def possible_attack_diagonal_down_right(self, row, col):
    #     if self.__board__.get_piece(row - 1, col + 1) is not None and self.__board__.get_piece(row - 1, col + 1).__color__ != self.__color__:
    #         return [(row - 1, col + 1)]
    #     return []
    

    # def possible_attack_diagonal_up_left(self, row, col):

    #     if self.__board__.get_piece(row + 1, col - 1) is not None and self.__board__.get_piece(row + 1, col - 1).__color__ != self.__color__:
    #         return [(row + 1, col - 1)]
    #     return []
    # def possible_attack_diagonal_up_right(self, row, col):
    #     if self.__board__.get_piece(row + 1, col + 1) is not None and self.__board__.get_piece(row + 1, col + 1).__color__ != self.__color__:
    #         return [(row + 1, col + 1)]
    #     return []
