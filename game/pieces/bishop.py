from .piece import Piece
class Bishop(Piece):
    white_str = "♝"
    black_str = "♗"

    def possible_positions(self, row, col):
        positions = []
        positions.extend(possible_positions_diagonal_up_left(self.board, row, col))
        positions.extend(possible_positions_diagonal_down_right(self.board, row, col))
        positions.extend(possible_positions_diagonal_down_left(self.board, row, col))
        positions.extend(possible_positions_diagonal_up_right(self.board, row, col))
        
        return positions