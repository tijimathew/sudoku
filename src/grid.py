from square import Square

class Grid:
    def __init__(self):
        self.rows = [Row() for i in range(9)]
        self.columns = [Column() for i in range(9)]
        self.boxes = [Box() for i in range(9)]
    

class Row:
    def __init__(self):
        self.squares = [Square() for i in range(9)]

class Column:
    def __init__(self):
        self.squares = [Square() for i in range(9)]

class Box:
    def __init__(self):
        self.squares = [Square() for i in range(9)]