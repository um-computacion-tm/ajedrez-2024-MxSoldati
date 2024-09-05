class PiceMovements:
    
    def movement_vertical_desc(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles
    
    def movement_vertical_asc(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles
    
    def movement_horizontal_right(self, row, col):
        possibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
    
    def movement_horizontal_left(self, row, col):
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
    
    #PAWN MOVEMENTS

    def movement_pawn_white(row, col):
        possibles = []
        if row == 1:
            possibles.append((row + 1, col))
            possibles.append((row + 2, col))
        else:
            possibles.append((row + 1, col))
        return possibles

    def movement_pawn_black(row, col):
        possibles = []
        if row == 6:
            possibles.append((row - 1, col))
            possibles.append((row - 2, col))
        else:
            possibles.append((row - 1, col))
        return possibles
    
    #Diagonal Movements
    #Quise hacerlo de forma individual

    def possible_positions_diagonal_up_left(row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row + i, col - i
            if next_row < 8 and next_col >= 0:
                possibles.append((next_row, next_col))
            else:
                break
        return possibles

    def possible_positions_diagonal_up_right(row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row + i, col + i
            if next_row < 8 and next_col < 8:
                possibles.append((next_row, next_col))
            else:
                break
        return possibles
    
    def possible_positions_diagonal_down_right(row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row - i, col + i
            if next_row >= 0 and next_col < 8:
                possibles.append((next_row, next_col))
            else:
                break
        return possibles
    
    def possible_positions_diagonal_down_left(row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row - i, col - i
            if next_row >= 0 and next_col >= 0:
                possibles.append((next_row, next_col))
            else:
                break
        return possibles
    
