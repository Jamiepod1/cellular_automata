import turtle as t

class Cell(t.Turtle):
    def __init__(self, rule=None):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.state = 0
        self.rule = rule

    def state_change(self):
        if self.state == 1:
            self.state = 0
            self.color("white")
        else:
            self.state = 1
            self.color("black")


if __name__ == '__main__':
    print("cell.py is being run directly")
