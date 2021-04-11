from square import Square

class Grid:
    def __init__(self):
        self._create_grid_squares()

    def clear(self):
        self._create_grid_squares()

    def _create_grid_squares(self):

        box_row = 0
        box_col = 0
        self.squares = []
        self.rows = [Row() for i in range(9)]
        self.cols = [Column() for i in range(9)]
        self.boxes = [Box() for i in range(9)]

        for grid_row in range(9):
            for grid_col in range(9):
                if grid_row % 3 == 0:
                    box_row = grid_row
                
                if grid_col % 3 == 0:
                    box_col = grid_col
                
                square = Square(grid_row, grid_col, box_row, box_col)

                self.rows[grid_row].squares[grid_col] = square
                self.cols[grid_col].squares[grid_row] = square
                self.squares[grid_row][grid_col] = square


class Row:
    def __init__(self):
        self.squares = []

class Column:
    def __init__(self):
        self.squares = []

class Box:
    def __init__(self):
        self.squares = []
    
    def link_squares(self, square):
        self.row = square.horizontal_box_number
        self.column = square.vertical_box_number
        self.squares.append(square)