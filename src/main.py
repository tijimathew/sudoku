import os

from grid import *

grid = Grid()
grid.print_grid()

running = True
while running:
    
    read_index = input('Enter row and column number as "Row#(1-9) Column#(1-9)" and press ENTER : ')
    x, y = read_index.split(' ')
    row = int(x) - 1
    column = int(y) - 1

    value = input('Enter the value (1-9) to be placed in the square you just chose and press ENTER : ')
    # validate the row, column and value before saving the square

    # if valid then assign value and reduce remaining count
    grid.squares[row][column].value = value
    grid.remaining_count -= 1

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    grid.print_grid()

    if grid.remaining_count <= 0:
        running = False