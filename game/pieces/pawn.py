from .piece import Piece
from ..movements import PiceMovements

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if self.__color__ == "WHITE":
            possible_positions = (
                self.possible_movement_vertical_down(from_row, from_col) + 
                self.possible_attack_diagonal_down(from_row, from_col) +
                self.possible_attack_diagonal_down_right(from_row, from_col)
            )
        else:
            possible_positions = (
                self.possible_movement_vertical_up(from_row, from_col) +
                self.possible_attack_diagonal_up_left(from_row, from_col) +
                self.possible_attack_diagonal_up_right(from_row, from_col)
            )
        return (to_row, to_col) in possible_positions


        
    def possible_movement_vertical_down(self, row, col, start_row=6):
        return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_down, start_row)
    def possible_movement_vertical_up(self, row, col, start_row=1):
        return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_up, start_row)
        
    def possible_movement_vertical(self, row, col, movement_func, start_row):
        import ipdb; ipdb.set_trace()
        if row == start_row and self.__board__.get_piece(row + 2 , col) == None:
            return movement_func(self, row, col)[:2]
        elif self.__board__.get_piece(row + 1 , col) == None:
            return movement_func(self, row, col)[:1]
        else:
            return []



    def possible_attack_diagonal_down_left(self, row, col):
        return self.possible_attack_diagonal(row, col, PiceMovements.movement_diagonal_down_left)
    def possible_attack_diagonal_down_right(self, row, col):
        return self.possible_attack_diagonal(row, col, PiceMovements.movement_diagonal_down_right)
    
    def possible_attack_diagonal_down(self, row, col, movement_func):
        return movement_func(self, row, col)[:1]


    #Para pawn blanco
    # def possible_movement_vertical_down(self, row, col):
    #     if row == 6:
    #         return PiceMovements.movement_vertical_down(self, row, col)[:2]
    #     else:
    #         return PiceMovements.movement_vertical_down(self, row, col)[:1]


    # #Para pawn negro

    # def possible_movement_vertical_up(self, row, col):
    #     if row == 1:
    #         return PiceMovements.movement_vertical_up(self, row, col)[:2]
    #     else:
    #         return PiceMovements.movement_vertical_up(self, row, col)[:1]


    def possible_attack_diagonal_down_left(self, row, col): 
        return [(),]
        


    def possible_attack_diagonal_down_right(self, row, col):
        return [(),]


    def possible_attack_diagonal_up_left(self, row, col):
        return [(),]
    
    def possible_attack_diagonal_up_right(self, row, col):
        return [(),]