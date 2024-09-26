from .piece import Piece


class Bishop(Piece):
    white_str = "♝"
    black_str = "♗"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.movement_diagonal(from_row, from_col, 1, 1) +
            self.movement_diagonal(from_row, from_col, 1, -1) +
            self.movement_diagonal(from_row, from_col, -1, 1) +
            self.movement_diagonal(from_row, from_col, -1, -1)
        )
        return (to_row, to_col) in possible_positions