from .piece import Piece


class Rook(Piece):
    white_str = "♜"
    black_str = "♖"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.movement_vertical_down(from_row, from_col) +
            self.movement_vertical_up(from_row, from_col) +
            self.movement_horizontal_right(from_row, from_col) +
            self.movement_horizontal_left(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions


