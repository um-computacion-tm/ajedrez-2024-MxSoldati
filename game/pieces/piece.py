class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def get_color(self):
        return self.__color__
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str




    def movement(self, row, col, row_direction, col_direction):
        possibles = []
        to_row = row + row_direction
        to_col = col + col_direction
        while 0 <= to_row < 8 and 0 <= to_col < 8:
            other_piece = self.__board__.get_piece(to_row, to_col)
            # print(f"Checking position ({to_row}, {to_col}): {other_piece}")  # Sirve para debuggear
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((to_row, to_col))
                break
            possibles.append((to_row, to_col))
            to_row += row_direction
            to_col += col_direction
        # print(f"Possible moves: {possibles}")
        return possibles

    def movement_vertical(self, row, col, direction):
        return self.movement(row, col, direction, 0)
    
    def movement_horizontal(self, row, col, direction):
        return self.movement(row, col, 0, direction)
    
    def movement_vertical_down(self, row, col):
        return self.movement_vertical(row, col, -1)

    def movement_vertical_up(self, row, col):
        return self.movement_vertical(row, col, 1)
    
    def movement_horizontal_right(self, row, col):
        return self.movement_horizontal(row, col, 1)

    def movement_horizontal_left(self, row, col):
        return self.movement_horizontal(row, col, -1)


    def movement_diagonal(self, row, col, row_direction, col_direction):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row + i * row_direction, col + i * col_direction
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
            else:
                break
        return possibles

    def movement_diagonal_up_left(self, row, col):
        return self.movement_diagonal(row, col, 1, -1)

    def movement_diagonal_up_right(self, row, col):
        return self.movement_diagonal(row, col, 1, 1)

    def movement_diagonal_down_right(self, row, col):
        return self.movement_diagonal(row, col, -1, 1)

    def movement_diagonal_down_left(self, row, col):
        return self.movement_diagonal(row, col, -1, -1)
    


    # def movement_diagonal_up_left(self, row, col):
    #     possibles = []
    #     for i in range(1, 8):
    #         next_row, next_col = row + i, col - i
    #         if next_row < 8 and next_col >= 0:
    #             other_piece = self.__board__.get_piece(next_row, next_col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((next_row, next_col))
    #                 break
    #             possibles.append((next_row, next_col))
    #         else:
    #             break
    #     return possibles

    # def movement_diagonal_up_right(self, row, col):
    #     possibles = []
    #     for i in range(1, 8):
    #         next_row, next_col = row + i, col + i
    #         if next_row < 8 and next_col < 8:
    #             other_piece = self.__board__.get_piece(next_row, next_col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((next_row, next_col))
    #                 break
    #             possibles.append((next_row, next_col))
    #         else:
    #             break
    #     return possibles

    # def movement_diagonal_down_right(self, row, col, vert_direction):
    #     possibles = []
    #     for i in range(1, 8):
    #         next_row, next_col = row - i, col + i
    #         if next_row >= 0 and next_col < 8:
    #             other_piece = self.__board__.get_piece(next_row, next_col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((next_row, next_col))
    #                 break
    #             possibles.append((next_row, next_col))
    #         else:
    #             break
    #     return possibles

    # def movement_diagonal_down_left(self, row, col):
    #     possibles = []
    #     for i in range(1, 8):
    #         next_row, next_col = row - i, col - i
    #         if next_row >= 0 and next_col >= 0:
    #             other_piece = self.__board__.get_piece(next_row, next_col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((next_row, next_col))
    #                 break
    #             possibles.append((next_row, next_col))
    #         else:
    #             break
    #     return possibles