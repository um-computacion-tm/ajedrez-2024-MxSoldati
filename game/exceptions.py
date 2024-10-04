class InvalidMove(Exception):
    message = "Movimiento de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"


class Tablas(Exception):
    message = "El juego se continua"
    def __str__(self):
        return self.message

class NoTablas(Tablas):
    message = "El juego se continua"
