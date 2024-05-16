import turtle as t
import time
from cell import Cell

screen = t.Screen()
screen.tracer(0)

#set up grid of cells
y_no_of_cells = 11
x_no_of_cells = 11
grid = []
starting_x = -int(x_no_of_cells/2) * 20
starting_y = int(y_no_of_cells/2) * 20


for y in range(y_no_of_cells):
    row = []
    x_coord = starting_x
    for x in range(x_no_of_cells):
        y_coord = starting_y
        cell = Cell()
        cell.goto(x_coord, y_coord)
        row.append(cell)
        x_coord += 20
    grid.append(row)
    starting_y -= 20
    

screen.update()

for row in grid:
    for cell in row:
        print(cell)

cell = Cell()
cell.state_change()


#set up rule






t.mainloop()