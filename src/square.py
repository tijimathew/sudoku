class Square:
    def __init__(self, grid_index_row:int, grid_index_column:int, box_index_row:int, box_index_column:int, value:int=None):
        self.value = value
        self.horizontal_row_number = grid_index_row
        self.vertical_column_number = grid_index_column
        self.horizontal_box_number = box_index_row
        self.vertical_box_number = box_index_column
