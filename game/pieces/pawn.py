from .piece import Piece
from ..movements import PiceMovements

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if self.__color__ == "WHITE":
            possible_positions = (
                self.possible_movement_vertical_down(from_row, from_col) +
                self.possible_attack_diagonal_down_left(from_row, from_col) +
                self.possible_attack_diagonal_down_right(from_row, from_col)
            )
        else:
            possible_positions(
                self.possible_movement_vertical_up(from_row, from_col) +
                self.possible_attack_diagonal_up_left(from_row, from_col) +
                self.possible_attack_diagonal_up_right(from_row, from_col)
            )
        return (to_row, to_col) in possible_positions

    #Para pawn blanco
    def possible_movement_vertical_down(self, row, col):
        if row == 6:
            return PiceMovements.movement_vertical_down(self, row, col)[:2]
        else:
            return PiceMovements.movement_vertical_down(self, row, col)[:1]

    def possible_attack_diagonal_down_left(self, row, col): 
        ...
        


    def possible_attack_diagonal_down_right(self, row, col):
        ...


    #Para pawn negro

    def possible_movement_vertical_up(self, row, col):
        if row == 1:
            return PiceMovements.movement_vertical_up(self, row, col)[:2]
        else:
            return PiceMovements.movement_vertical_up(self, row, col)[:1]



    def possible_attack_diagonal_up_left(self, row, col):
        ...
    
    def possible_attack_diagonal_up_right(self, row, col):
        # possible = []
        # if PiceMovements.movement_diagonal_up_right(self, row, col)[:1] != None:
        #     possible.extend.PiceMovements.movement_diagonal_up_right(self, row, col)[:1]
        # return possible
        ...