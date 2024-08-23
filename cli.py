from chess import Chess
from exceptions import InvalidMove

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        # :)
        #antes de mover la pieza, validar si la pieza se puede mover
        chess.validate_coords(from_row, from_col)
        chess.validate_coords(to_row, to_col)
        #si la pieza se valida, moverla
        chess.move(from_row, from_col, to_row, to_col)
    except InvalidMove as e:
        print("Invalid move", e)
    except Exception as e:           ## Aca atrapamos todas las excepciones que se produzcan
        print("error", e)


if __name__ == '__main__':
    main()