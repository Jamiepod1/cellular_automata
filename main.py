import turtle as t
import time
from cell import Cell
import random
import statistics
import matplotlib.pyplot as plt

screen = t.Screen()
screen.tracer(0)
y_no_of_cells = 395
x_no_of_cells = 395
#set up grid of cells

def setup_grid(x_number, y_number):

    grid = []
    starting_x = -int(x_number/2) * 2.5
    starting_y = int(y_number/2) * 2.5


    for y in range(y_no_of_cells):
        row = []
        x_coord = starting_x
        for x in range(x_no_of_cells):
            y_coord = starting_y
            cell = Cell()
            cell.goto(x_coord, y_coord)
            row.append(cell)
            x_coord += 2.5
        grid.append(row)
        starting_y -= 2.5
    return grid

grid = setup_grid(x_no_of_cells, y_no_of_cells)



#set up rule
def ruleset(left_neighbour, cell, right_neighbour, output_pattern):
    cell_neighbourhood = (left_neighbour, cell, right_neighbour)
    if cell_neighbourhood == (0, 0, 0):
        return int(output_pattern[0])
    elif cell_neighbourhood == (0, 0, 1):
        return int(output_pattern[1])
    elif cell_neighbourhood == (0, 1, 0):
        return int(output_pattern[2])
    elif cell_neighbourhood == (0, 1, 1):
        return int(output_pattern[3])
    elif cell_neighbourhood == (1, 0, 0):
        return int(output_pattern[4])
    elif cell_neighbourhood == (1, 0, 1):
        return int(output_pattern[5])
    elif cell_neighbourhood == (1, 1, 0):
        return int(output_pattern[6])
    elif cell_neighbourhood == (1, 1, 1):
        return int(output_pattern[7])


def generate(ruleset_output_pattern):
    global grid
    generation = 0
    for row_index in range(len(grid)):
        for index in range(1, len(grid[0]) - 1):
            if generation == 0:
                centre_cell = int(len(grid[0])/2)
                if grid[row_index][index] == grid[row_index][centre_cell]:
                    grid[row_index][index].change_state(1)
            else:
                left_neighbour_index = index - 1
                left_neighbour_state = grid[row_index - 1][left_neighbour_index].state
                right_neighbour_index = index + 1
                right_neighbour_state = grid[row_index - 1][right_neighbour_index].state
                cell_state = grid[row_index - 1][index].state
                new_state = ruleset(left_neighbour_state, cell_state, right_neighbour_state, ruleset_output_pattern)
                grid[row_index][index].change_state(new_state)
        generation += 1


def wipe():
    global grid
    for row in grid:
        for cell in row:
            cell.change_state(0)

def count_on_state():
    global grid
    total_cells = 0
    on_cells = 0
    for row in grid:
        for cell in row:
            total_cells += 1
            on_cells += cell.state
    return on_cells

def generate_output_patterns(repeats):
    testing_dict = {}

    for on_state_count in range(0, 9):
        off_state_count = 8 - on_state_count
        testing_dict[on_state_count] = []

        for repeat in range(repeats):
            output_pattern = ""
            for _ in range(on_state_count):
                output_pattern += "1"
            for _ in range(off_state_count):
                output_pattern += "0"
            char_list = list(output_pattern)
            random.shuffle(char_list)
            output_pattern = "".join(char_list)
            testing_dict[on_state_count].append(output_pattern)

    return testing_dict

def generate_bit_pattern():
    num_bits = 8
    testing_dict = {key: [] for key in range(0, num_bits + 1)}
    print(testing_dict)

    max_val = 2 ** num_bits  # This is 512, which is 2^9
    
    bit_patterns = []
    for i in range(max_val):
        # Format the number as binary, fill with leading zeros to ensure it's always 9 bits
        pattern = f"{i:09b}"  # 09b means 9 bits with leading zeros in binary format
        bit_patterns.append(pattern)
    
    for pattern in bit_patterns:
        testing_dict[pattern.count("1")].append(pattern)

    return testing_dict

generate("010100101")
screen.update()
#test_pattern_visualiser = t.Turtle()
#test_pattern_visualiser.penup()
#test_pattern_visualiser.goto(300, 0)
#test_pattern_visualiser.hideturtle()

#testing_dict = generate_bit_pattern()
#for on_count in range(1, len(testing_dict)):
#    for test_pattern in testing_dict[on_count]:
#        generate(test_pattern)
#        test_pattern_visualiser.write(test_pattern)
 #       screen.update()
 #       time.sleep(0.5)
 #       test_pattern_visualiser.clear()
 #       wipe()



#setup_grid(x_no_of_cells, y_no_of_cells)
#testing_dict = generate_bit_pattern()
#results = []
#for on_count in range(0, len(testing_dict)):
#    to_average = []
 #   for test_pattern in testing_dict[on_count]:
 #       generate(test_pattern)
 #       screen.update()
 #       to_average.append(count_on_state())
 #       time.sleep(5)
 #       wipe()

  #  results.append(statistics.mean(to_average))
    

# Data
#categories = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

# Create a bar chart
#plt.bar(categories, results)

# Adding title and labels
#plt.title('Simple Bar Chart')
#plt.xlabel('Categories')
#plt.ylabel('Values')

# Show the plot
#plt.show()






t.mainloop()