from .piece import Piece


class King(Piece):
    white_str = "♚"
    black_str = "♔"
        

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = ( 
            self.movement_vertical(from_row, from_col, 1)[:1] +
            self.movement_vertical(from_row, from_col, -1)[:1] +
            self.movement_horizontal(from_row, from_col, -1)[:1] +
            self.movement_horizontal(from_row, from_col, 1)[:1] +
            self.movement_diagonal(from_row, from_col, -1, -1)[:1] +
            self.movement_diagonal(from_row, from_col, -1, 1)[:1] +
            self.movement_diagonal(from_row, from_col, 1, -1)[:1] +
            self.movement_diagonal(from_row, from_col, 1, 1)[:1]
        )

        return (to_row, to_col) in possible_positions

    def movement_vertical_down(self, row, col):
        return self.movement_vertical(row, col, -1)[:1]
    
    def movement_vertical_up(self, row, col):
        return self.movement_vertical(row, col, 1)[:1]
    
    def movement_horizontal_left(self, row, col):
        return self.movement_horizontal(row, col, -1)[:1]  
    
    def movement_horizontal_right(self, row, col):
        return self.movement_horizontal(row, col, 1)[:1]
    
    def possible_movement_diagonal_down_left(self, row, col):
        return self.movement_diagonal(row, col, -1, -1)[:1]
    
    def possible_movement_diagonal_down_right(self, row, col):
        return self.movement_diagonal(row, col, -1, 1)[:1]
    
    def possible_movement_diagonal_up_left(self, row, col):
        return self.movement_diagonal(row, col, 1, -1)[:1]
    
    def possible_movement_diagonal_up_right(self, row, col):
        return self.movement_diagonal(row, col, 1, 1)[:1]