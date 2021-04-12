from grid import *

grid = Grid()
running = True

while running:
    
    grid.print_grid()
    grid.remaining_count = 0
    read_index = input('Enter row and column number as "Row Column" : ')
    row, column = read_index.split(' ')
    row = int(row) - 1
    column = int(column) - 1

    value = input('Enter the value of the square you just chose [0-9] : ')
    # validate the row, column and value before saving the square

    # if valid then assign value and reduce remaining count
    grid.squares[row][column].value = value
    grid.remaining_count -= 1

    if grid.remaining_count <= 0:
        running = False