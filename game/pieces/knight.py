from .piece import Piece

class Knight(Piece):
    white_str = "♞"
    black_str = "♘"

    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.possible_positions_knight(from_row, from_col)
        return (to_row, to_col) in possible_positions
    
    def possible_positions_knight(self, row, col):
        possibles = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        # import ipdb; ipdb.set_trace()
        for move in knight_moves: # move son las tuplas de knight_moves, donde las recorremos individualmente
            new_row, new_col = row + move[0], col + move[1] # nuevas posiciones son los siguientes movimientos ; donde sumamos la primera 
            # fila/columna con la tupla (que son los possibles movimientos, de forma individual)
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # vemos que onda con las nuevas posiciones, si se pasan del board
                other_piece = self.__board__.get_piece(new_row, new_col) # si hay otra pieza, que no se pueda mover
                if other_piece is None or other_piece.__color__ != self.__color__: # si no hay pieza o si la pieza es de otro color
                    possibles.append((new_row, new_col)) 

        return possibles