from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_turtle()
        self.snake_head = self.all_turtle[0]

    def create_turtle(self):
        for core in COORDINATES:
            self.add_segment(core)

    def add_segment(self, core):
        tom = Turtle(shape="square")
        tom.penup()
        tom.color("white")
        tom.goto(core)
        self.all_turtle.append(tom)

    def extend(self):
        #add new segment to the snake.
        self.add_segment(self.all_turtle[-1].position())

    def move(self):
        for square in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[square - 1].xcor()
            new_y = self.all_turtle[square - 1].ycor()
            self.all_turtle[square].goto(new_x, new_y)
        self.snake_head.fd(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
