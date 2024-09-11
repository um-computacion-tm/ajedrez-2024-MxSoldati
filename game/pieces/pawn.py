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


        
    def possible_movement_vertical_down(self, row, col, start_row=6): # como parametro preguntamos si es el primer movimiento o no
        return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_down, start_row) 
    def possible_movement_vertical_up(self, row, col, start_row=1):
        return self.possible_movement_vertical(row, col, PiceMovements.movement_vertical_up, start_row)  
    # con estas funciones podemos unir sus movimientos verticales, para que quede bien refactorizado, fua la forma con la que siento que sirve
    # Usamos una funcion como parametro para ver que movimiento vertical es, nueva implementacion de parametros en funciones.
    # Se puede hacer con un if, pero no lo veo tan limpio como con esta forma de hacerlo
        
    def possible_movement_vertical(self, row, col, movement_func, start_row): # aca traemos esa funcion (movement_func) como parametro
        # import ipdb; ipdb.set_trace()
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







    def possible_attack_diagonal_down_left(self, row, col): 
        return [(),]
    def possible_attack_diagonal_down_right(self, row, col):
        return [(),]
    def possible_attack_diagonal_up_left(self, row, col):
        return [(),]
    def possible_attack_diagonal_up_right(self, row, col):
        return [(),]