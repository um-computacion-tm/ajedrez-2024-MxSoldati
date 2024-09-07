class PiceMovements:
    
    def movement_vertical_up(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            # print(f"Checking position ({next_row}, {col}): {other_piece}") Sirve para debuggear 
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        # print(f"Possible moves: {possibles}")
        return possibles
    
    def movement_vertical_down(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            # print(f"Checking position ({next_row}, {col}): {other_piece}")
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        # print(f"Possible moves: {possibles}")
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
    
    #Diagonal Movements
    #Quise hacerlo de forma individual

    def possible_positions_diagonal_up_left(self, row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row + i, col - i
            if next_row < 8 and next_col >= 0:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
            else:
                break
        return possibles

    def possible_positions_diagonal_up_right(self, row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row + i, col + i
            if next_row < 8 and next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
            else:
                break
        return possibles

    def possible_positions_diagonal_down_right(self, row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row - i, col + i
            if next_row >= 0 and next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
            else:
                break
        return possibles

    def possible_positions_diagonal_down_left(self, row, col):
        possibles = []
        for i in range(1, 8):
            next_row, next_col = row - i, col - i
            if next_row >= 0 and next_col >= 0:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
            else:
                break
        return possibles


    #Pawn Movements
    #Llamo a las funciones de los movimientos ya creados, y se los encajo a los peones

    def possible_positions_pawn_white(self, row, col):
        possibles = []
        if row == 6:  # Movimiento inicial del peón blanco
            possibles.extend(self.movement_vertical_down(row, col)[:2])
        else:
            possibles.extend(self.movement_vertical_down(row, col)[:1])

        # Movimiento de ataque en diagonal
        possibles.extend(self.possible_positions_diagonal_down_left(row, col))
        possibles.extend(self.possible_positions_diagonal_down_right(row, col))

        return possibles

    def possible_positions_pawn_black(self, row, col):
        possibles = []
        if row == 1:  # Movimiento inicial del peón negro
            possibles.extend(self.movement_vertical_up(row, col)[:2])
        else:
            possibles.extend(self.movement_vertical_up(row, col)[:1])

        # Movimiento de ataque en diagonal
        possibles.extend(self.possible_positions_diagonal_up_left(row, col))
        possibles.extend(self.possible_positions_diagonal_up_right(row, col))

        return possibles