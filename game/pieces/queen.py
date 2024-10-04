from .piece import Piece


class Queen(Piece):
    white_str = "♛"
    black_str = "♕"


    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.movement_vertical(from_row, from_col, 1) +
            self.movement_vertical(from_row, from_col, -1) +
            self.movement_horizontal(from_row, from_col, 1) +
            self.movement_horizontal(from_row, from_col, -1) +
            
            self.movement_diagonal_up_left(from_row, from_col) +
            self.movement_diagonal_up_right(from_row, from_col) +
            self.movement_diagonal_down_right(from_row, from_col) +
            self.movement_diagonal_down_left(from_row, from_col)

        )
        return (to_row, to_col) in possible_positions
    
    
    
