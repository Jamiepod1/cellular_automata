import turtle as t
from cell import Cell

class CellularAutomaton(Cell):
    def __init__(self, cell_array_size, num_of_generations) -> None:
        self.grid = None
        self.cell_array_size = cell_array_size
        self.num_of_generations = num_of_generations


    def setup_grid(self):

        self.grid = []
        starting_x = -int(self.cell_array_size/2) * 10
        starting_y = int(self.num_of_generations/2) * 10


        for y in range(self.num_of_generations):
            row = []
            x_coord = starting_x
            for x in range(self.cell_array_size):
                y_coord = starting_y
                cell = Cell()
                cell.goto(x_coord, y_coord)
                row.append(cell)
                x_coord += 10
            self.grid.append(row)
            starting_y -= 10



    def ruleset(three_bit_neighbourhood_representation: str, output_pattern: str):
        base_10_neighbourhood_representation = int(three_bit_neighbourhood_representation, 2)
        return output_pattern[base_10_neighbourhood_representation]

screen = t.Screen()
screen.tracer(0)
instance = CellularAutomaton(51,51)
instance.setup_grid()
#for _ in instance.grid:
#    print(_)
screen.update()
print("updated")

t.mainloop()

