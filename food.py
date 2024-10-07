from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("yellow")
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)

    def refresh(self):
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)


