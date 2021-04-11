class Grid:
    def __init__(self):
        GRID_ROWS = GRID_COLUMNS = 9
        BOX_ROWS = BOX_COLUMNS = 3
        self.squares = [[Square(row, column) for column in range(GRID_COLUMNS)] for row in range(GRID_ROWS)]
        self.boxes = [[Box(row, column) for column in range(BOX_COLUMNS)] for row in range(BOX_ROWS)]
        self.rows = [Row() for row in range(GRID_ROWS)]


class Square:
    def __init__(self, row, column):
        self.grid_row_index = row
        self.grid_column_index = column
        self.box_row_index = None
        self.box_column_index = None
        self.value = None

class Row:
    pass

class Column:
    pass

class Box:
    def __init__(self, row, column):
        self.box_row_index = row
        self.box_column_index = column