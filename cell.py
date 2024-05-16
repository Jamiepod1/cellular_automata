import turtle as t

class Cell(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.state = 0
        self.shapesize(stretch_wid=1, stretch_len=1, outline=0)
        self.penup()

    def __str__(self):
        return f"{self.xcor()}, {self.ycor()}"
    

    def on(self):
        if self.state == 0:
            self.state = 1
            self.color("black")


    def off(self):
        if self.state == 1:
            self.state = 0
            self.color("white")


if __name__ == '__main__':
    print("cell.py is being run directly")
