import turtle as t

class Cell(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.state = 0
        self.shapesize(stretch_wid=1, stretch_len=1, outline=0)
        self.penup()

    def __repr__(self):
        return f"{self.xcor()}, {self.ycor()}"
    

    def change_state(self, state):
        self.state = state
        if self.state == 0:
            self.color("white")
        elif self.state == 1:
            self.color('black')


if __name__ == '__main__':
    print("cell.py is being run directly")
