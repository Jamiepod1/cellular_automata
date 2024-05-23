from cellular_automaton import CellularAutomaton
import turtle as t
import sys

mode = None

try:
    if sys.argv[1] == "binary":
        try:
            output_pattern = int(sys.argv[2])
        except IndexError:
            output_pattern = int(input("Enter output pattern (0-255)"))
        finally:
            mode = sys.argv[1]
        
    elif sys.argv[1] == "rgb":
        mode = sys.argv[1]
        output_pattern = None

except IndexError:
    print("Must provide argument: 'rgb' or 'binary'")

else:
    screen = t.Screen()
    screen.tracer(0)
    instance = CellularAutomaton(321,321, sys.argv[1])
    instance.setup_grid()
    instance.generate(output_pattern)

    screen.update()
    t.mainloop()