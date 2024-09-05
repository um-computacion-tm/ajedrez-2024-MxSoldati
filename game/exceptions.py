class InvalidMove(Exception):
    ...

class InvalidMoveNoPiece(InvalidMove):
    ...

class InvalidMoveRookMove(InvalidMove):
    ...

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"
