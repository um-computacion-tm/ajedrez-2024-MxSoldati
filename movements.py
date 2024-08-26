from abc import ABC, abstractmethod
from cli import play

class PieceMovement(ABC):
    @abstractmethod
    def puede_mover(self, from_row, from_col, to_row, to_col):
        ...

class RookMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if from_row == to_row or from_col == to_col:
            return True
        else:
            return ValueError("Movimiento no permitido")

class PawnMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if from_col == to_col and (from_row - to_row == 1 or (from_row == 6 and from_row - to_row == 2)):
            return True
        else:
            return ValueError("Movimiento no permitido")

class HorseMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2):
            return True
        else:
            return False

class BishopMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if abs(from_row - to_row) == abs(from_col - to_col):
            return True
        else:
            return False

class QueenMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if from_row == to_row or from_col == to_col or abs(from_row - to_row) == abs(from_col - to_col):
            return True
        else:
            return False

class KingMovement(PieceMovement):
    def puede_mover(self, from_row, from_col, to_row, to_col):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True
        else:
            return False

# Implementar otras clases que faltan

class Chess:
    def __init__(self):
        self.movements = {}
    
    def add_movement(self):
        ...
        #aca agregamos la pieza que queremos mover
        #de forma generica 
        #ejemplo:
        #quiero mover una torre
        # y la quiero mover en la posicion X,Y
        
    def move(self):
        ...
        #aca vamos a hacer el movimiento de las piezas
        #de forma generica
        #ejemplo:
        #Se que quiero mover una torre
        # y se donde la quiero mover(X,Y)
        # Ver si esa pieza se puede mover a esa posicion
        # Si se puede mover, moverla 
        #sino raise un error




