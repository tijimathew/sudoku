GRID_ROWS = GRID_COLUMNS = 9
BOX_ROWS = BOX_COLUMNS = 3

class Grid:
    def __init__(self):
        
        self.squares = self._create_grid_squares()
        self.boxes = self._create_grid_boxes()
        self.rows = self._create_grid_rows()
        self.columns = self._create_grid_columns()
        self.row_count = len(self.rows)
        self.column_count = len(self.columns)
        self.box_count = len(self.boxes) * len(self.boxes[0])
        self.remaining_count = self.row_count * self.column_count
    

    def clear(self):
        self.squares = self._create_grid_squares()
        self.boxes = self._create_grid_boxes()
        self.rows = self._create_grid_rows()
        self.columns = self._create_grid_columns()

    def _create_grid_squares(self):
        return [[Square(row, column) for column in range(GRID_COLUMNS)] for row in range(GRID_ROWS)]

    def _create_grid_boxes(self):
        return [[Box(row, column) for column in range(BOX_COLUMNS)] for row in range(BOX_ROWS)]

    def _create_grid_rows(self):
        return [Row(row) for row in range(GRID_ROWS)]

    def _create_grid_columns(self):
        return [Column(column) for column in range(GRID_COLUMNS)]

    def print_grid(self):

        print(" ", end=" ")

        for column in range(9):
            print("  " + str(column + 1), end=" ")
        
        print("\n")
        
        for row in range(9):
            for column in range(9):
                if column == 0: 
                    print(str(row + 1), end=" ")    

                square_value = self.squares[row][column].value
                if square_value not in range(1,10):
                    square_value = "?"

                print("| " + str(square_value), end=" ")
            
            print("|\n")

class Square:
    def __init__(self, row, column):
        self.grid_index = (row, column)
        self.grid_row_index = row
        self.grid_column_index = column
        self.box_row_index = row // 3
        self.box_column_index = column // 3
        self.box_index = (row // 3, column // 3)
        self.value = 0

class Row:


    def __init__(self, row):

        self.grid_row = row
        self.square_indices = self._create_square_indices()
        self.count = len(self.square_indices)
    
    def _create_square_indices(self):
        return [(self.grid_row, column) for column in range(GRID_COLUMNS)]


class Column:


    def __init__(self, column):

        self.grid_column = column
        self.square_indices = self._create_square_indices()
        self.count = len(self.square_indices)
    

    def _create_square_indices(self):
        return [(row, self.grid_column) for row in range(GRID_ROWS)]

class Box:


    def __init__(self, row, column):

        self.grid_box_index = (row, column)
        self.grid_box_row_index = row
        self.grid_box_column_index = column
        self.square_indices = self._create_square_indices()
        self.count = len(self.square_indices)


    def _create_square_indices(self):

        square_indices = []
        for row in range(self.grid_box_row_index*3, (self.grid_box_row_index + 1)*3):
            for column in range(self.grid_box_column_index*3, (self.grid_box_column_index + 1)*3):
                square_indices.append((row, column))
        
        return square_indices

if __name__ == '__main__':
    grid = Grid()
    grid.print_grid()