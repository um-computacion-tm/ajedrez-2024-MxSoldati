from game.chess import Chess
from game.exceptions import InvalidMove

##### PARA CORRER EL JUEGO 'python3 -m game.cli' #####

def main():
    chess = Chess()
    while True:
        play(chess)
        if not chess.is_playing:
            break

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)

        from_row = input("From row: ")
        
        # Verificar si from_row es un número
        if from_row.isdigit():
            from_row = int(from_row)
            from_col = int(input("From col: "))
            to_row = int(input("To Row: "))
            to_col = int(input("To Col: "))
            # Sigue el camino normal

            chess.move (from_row, from_col, to_row, to_col)
        else:
            # Llamar a la función tablas si from_row no es un número
            chess.tablas(from_row)
            chess.is_playing = False



        
        # Mover la pieza
        

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