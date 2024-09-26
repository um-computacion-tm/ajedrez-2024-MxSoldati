from game.chess import Chess
from game.exceptions import InvalidMove

##### PARA CORRER EL JUEGO 'python3 -m game.cli' #####

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
        
        # Mover la pieza
        chess.move (from_row, from_col, to_row, to_col)

        # Ver si hay ganador
        winner = chess.determine_winner()
        if winner != "No winner yet":
            print(winner)
            chess.is_playing = False

    except InvalidMove as e:
        print("Invalid move:", e)
    except Exception as e:
        print("Error:", e)
    

if __name__ == '__main__':
    main()