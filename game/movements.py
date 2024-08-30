# movements.py
class PiceMovements:

    #VERTICAL MOVEMENTS

    def movement_vertical_desc(row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            possibles.append((next_row, col))
        return possibles

    def movement_vertical_asc(row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
    
    #HORIZONTAL MOVEMENTS
    def movement_horizontal_right(row, col):
        possibles = []
        for next_col in range(col + 1, 8):
            possibles.append((row, next_col))
        return possibles
    
    def movement_horizontal_left(row, col):
        possibles = []
        for next_col in range(col - 1, -1, -1):
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
