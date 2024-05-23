import turtle as t

class Cell(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.state = 0
        self.mode = "binary"
        self.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=0)
        self.penup()

    def __repr__(self):
        return f"{self.xcor()}, {self.ycor()}"
    

    def change_state(self, state: int):
        self.state = state
        if self.state == 0:
            self.color("white")
        elif self.state == 1:
            self.color('black')

    def rgb_colour_set(self, state):
        self.state = state
        if self.state == 0:
            self.color("black")
        elif self.state == 1:
            self.color("blue")
        elif self.state == 2:
            self.color("green")
        elif self.state == 3:
            self.color("cyan")
        elif self.state == 4:
            self.color("red")
        elif self.state == 5:
            self.color("magenta")
        elif self.state == 6:
            self.color("yellow")
        elif self.state == 7:
            self.color("white")


        

if __name__ == '__main__':
    print("cell.py is being run directly")
