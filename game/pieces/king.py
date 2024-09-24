from .piece import Piece


class King(Piece):
    white_str = "♚"
    black_str = "♔"
        
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = ( 
            self.movement_vertical_up(from_row, from_col) +
            self.movement_vertical_down(from_row, from_col) +
            self.movement_horizontal_left(from_row, from_col) +
            self.movement_horizontal_right(from_row, from_col) +
            self.possible_movement_diagonal_down_left(from_row, from_col) +
            self.possible_movement_diagonal_down_right(from_row, from_col) +
            self.possible_movement_diagonal_up_left(from_row, from_col) +
            self.possible_movement_diagonal_up_right(from_row, from_col)
        )

        return (to_row, to_col) in possible_positions

    def movement_vertical_down(self, row, col):
        return self.movement_vertical_down(self, row, col)[:1]
    
    def movement_vertical_up(self, row, col):
        return self.movement_vertical_up(self, row, col)[:1]
    
    def movement_horizontal_left(self, row, col):
        #print(f'esto es el mov {self.movement_horizontal_left(self, row, col)[:1]}')
        return self.movement_horizontal_left(self, row, col)[:1]  
    
    def movement_horizontal_right(self, row, col):
        return self.movement_horizontal_right(self, row, col)[:1]
    
    def possible_movement_diagonal_down_left(self, row, col):
        return self.movement_diagonal_down_left(self, row, col)[:1]
    
    def possible_movement_diagonal_down_right(self, row, col):
        return self.movement_diagonal_down_right(self, row, col)[:1]
    
    def possible_movement_diagonal_up_left(self, row, col):
        return self.movement_diagonal_up_left(self, row, col)[:1]
    
    def possible_movement_diagonal_up_right(self, row, col):
        return self.movement_diagonal_up_right(self, row, col)[:1]
    

    