import turtle as t
from cell import Cell
from random import randint

class CellularAutomaton():
    def __init__(self, cell_array_size, num_of_generations, mode) -> None:
        if mode not in ["rgb", "binary"]:
            raise ValueError(f"Invalid mode '{mode}'. Mode must be 'rgb' or 'binary'.")
        self.mode = mode
        self.grid = None
        self.cell_array_size = cell_array_size
        self.num_of_generations = num_of_generations
        self.rgb_decode_list = []
        self.bit_512_list = []


    def setup_grid(self):

        self.grid = []
        starting_x = -int(self.cell_array_size/2) * 2.5
        starting_y = int(self.num_of_generations/2) * 2.5


        for y in range(self.num_of_generations):
            row = []
            x_coord = starting_x
            for x in range(self.cell_array_size):
                y_coord = starting_y
                cell = Cell()
                cell.goto(x_coord, y_coord)
                row.append(cell)
                x_coord += 2.5
            self.grid.append(row)
            starting_y -= 2.5



    def ruleset(self, three_bit_neighbourhood_representation: str, output_pattern: str):
        base_10_neighbourhood_representation = int(three_bit_neighbourhood_representation, 2)
        return int(output_pattern[(base_10_neighbourhood_representation-7)*-1])
    

    def rgb_ruleset(self, three_bit_base_8_representation):
        if self.rgb_decode_list == []:
            for r in range(0, 8):
                for g in range(0, 8):
                    for b in range(0, 8):
                        self.rgb_decode_list.append(f"{r}{g}{b}")


        for index, decode in enumerate(self.rgb_decode_list):
            if decode == three_bit_base_8_representation:
                return self.bit_512_list[index]


    def list_generate(self):
        for _ in range(0, 512):
            self.bit_512_list.append(randint(0, 7))
            


    

    def generate(self, output_pattern=None):
        #if type(output_pattern) == int:
            #output_pattern = f"{output_pattern:08b}"
            #print(output_pattern)
        if self.mode == "rgb":
            self.list_generate()
        else:
            if type(output_pattern) == int:
                print(output_pattern)
                output_pattern = f"{output_pattern:08b}"
                print(output_pattern)
        generation = 0
        for row_index in range(len(self.grid)):
            for index in range(0, len(self.grid[0])):

                #Initialise the first generation and set the state of the middle cell to ON/white

                if generation == 0:
                    centre_cell = int(len(self.grid[0])/2)
                    if self.grid[row_index][index] == self.grid[row_index][centre_cell]:
                        if self.mode == "binary":
                            self.grid[row_index][index].change_state(1)
                        else:
                            self.grid[row_index][index].rgb_colour_set(7)

                #Code for all generations following gen 0
                
                else:
                    left_neighbour_index = index - 1
                    left_neighbour_state = self.grid[row_index - 1][left_neighbour_index].state
                    if self.grid[row_index - 1][index] == self.grid[row_index - 1][-1]:
                        right_neighbour_index = 0
                    else:
                        right_neighbour_index = index + 1
                    right_neighbour_state = self.grid[row_index - 1][right_neighbour_index].state
                    cell_state = self.grid[row_index - 1][index].state
                    three_bit_neighbourhood_number = f"{left_neighbour_state}{cell_state}{right_neighbour_state}"

                    if self.mode == "rgb":
                        new_state = self.rgb_ruleset(three_bit_neighbourhood_number)
                        self.grid[row_index][index].rgb_colour_set(new_state)
                    else:
                        new_state = self.ruleset(three_bit_neighbourhood_number, output_pattern)
                        self.grid[row_index][index].change_state(new_state)
            generation += 1
            


if __name__ == '__main__':
    print("cellular_automaton.py is being run directly")
