from .piece import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"
    __start_row__ = None

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_movement_vertical(from_row, from_col) + 
            self.possible_attack_diagonal(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def possible_movement_vertical(self, row, col):
        direction = -1 if self.__color__ == "WHITE" else 1
        start_row = 6 if self.__color__ == "WHITE" else 1
        possibles = []
        if row == start_row and self.__board__.get_piece(row + 2 * direction, col) is None and self.__board__.get_piece(row + 1 * direction, col) is None:
            possibles.extend([(row + 1 * direction, col), (row + 2 * direction, col)])
        elif self.__board__.get_piece(row + 1 * direction, col) is None:
            possibles.append((row + 1 * direction, col))
        return possibles

    def possible_attack_diagonal(self, row, col):
        direction = -1 if self.__color__ == "WHITE" else 1
        return self.possible_attack_diagonal_direction(row, col, direction, -1) + \
               self.possible_attack_diagonal_direction(row, col, direction, 1)

    def possible_attack_diagonal_direction(self, row, col, row_offset, col_offset):
        target_row = row + row_offset
        target_col = col + col_offset
        if 0 <= target_row < 8 and 0 <= target_col < 8:
            piece = self.__board__.get_piece(target_row, target_col)
            if piece is not None and piece.__color__ != self.__color__:
                return [(target_row, target_col)]
        return []